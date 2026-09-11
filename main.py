from PySide6.QtWidgets import QApplication, QWidget
from PySide6.QtGui import QTextCharFormat, QColor
from PySide6.QtCore import QObject, Signal, Qt, QMetaObject
import sys
import re
import threading
from datetime import datetime
from ui.ui_main import Ui_Form
from src.piano.config import PianoConfigPresets, PianoConfig
from src.util import Logger
from src.piano import piano_main
from pathlib import Path


class LogEmitter(QObject):
    log_signal = Signal(str, str) # (text, color)
    progress_signal = Signal(float)

class PianoLogger(Logger):
    def __init__(self) -> None:
        super().__init__()
        self.emitter = LogEmitter()

    def log(self, msg, color="#cccccc"):
        self.emitter.log_signal.emit(msg, color)

    def log_info(self, msg):
        self.log(f"\n[{datetime.now().strftime("%H:%M:%S")} | INFO] {msg}", "#cccccc")

    def log_success(self, msg):
        self.log(f"\n[{datetime.now().strftime("%H:%M:%S")} | INFO] {msg}", "#4fc14f")

    def log_error(self, msg):
        self.log(f"\n[{datetime.now().strftime("%H:%M:%S")} | ERROR] {msg}", "#ff5555")

    def log_warn(self, msg):
        self.log(f"\n[{datetime.now().strftime("%H:%M:%S")} | WARN] {msg}", "#ffdd44")

    def set_progress(self, process: float):
        self.emitter.progress_signal.emit(process)


def scan_resources_files(resources_dir: str | Path, suffix_list: list[str]) -> list[tuple[str, str]]:
    """
    -> [(FileName, Path), ...]
    """
    res_path = Path(resources_dir)
    res_path.mkdir(parents=True, exist_ok=True)
    result = []
    for file in res_path.iterdir():
        if file.is_file() and file.suffix.lower() in suffix_list:
            result.append((file.name, str(file)))
    result.sort(key=lambda x: x[0].lower())
    return result


class VAGWindow(QWidget):
    export_finish_signal = Signal()

    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)

        self.piano_logger = PianoLogger()
        self.piano_logger.emitter.log_signal.connect(self.on_log_receive)
        self.piano_logger.emitter.progress_signal.connect(self.on_progress_receive)
        self.export_finish_signal.connect(self.on_export_finish)

        self.is_exporting = False

        self.block_file_list: list[tuple[str, str]] = []
        self.midi_file_list: list[tuple[str, str]] = []

        self.ui.comboBox.clear()
        self.ui.comboBox.addItems(["大型方块键盘", "小型键盘", "涡旋键盘", "大型键盘"])
        self.ui.comboBox_4.addItems(["竖直", "水平"])
        self.piano_load_preset(0)
        self.piano_update_block_files(True)
        self.piano_update_midi_files(True)

        self.ui.comboBox.currentIndexChanged.connect(self.piano_load_preset)
        self.ui.pushButton.clicked.connect(self.piano_output)
        self.ui.pushButton_2.clicked.connect(self.piano_update_midi_files)
        self.ui.pushButton_3.clicked.connect(self.piano_update_block_files)

    def on_log_receive(self, msg, color):
        fmt = QTextCharFormat()
        qcolor = QColor(color)
        if not qcolor.isValid():
            qcolor = QColor("#cccccc")
        fmt.setForeground(qcolor)
        cursor = self.ui.plainTextEdit.textCursor()
        cursor.insertText(msg, fmt)
        self.ui.plainTextEdit.setTextCursor(cursor)
        self.ui.plainTextEdit.verticalScrollBar().setValue(self.ui.plainTextEdit.verticalScrollBar().maximum())

    def on_progress_receive(self, process: float):
        self.ui.progressBar.setValue(round(process * 100))

    def piano_update_block_files(self, checked: bool):
        self.ui.comboBox_2.clear()
        self.block_file_list = scan_resources_files("resources", [".schem", ".txt"])
        name_list = [name for name, _ in self.block_file_list]
        self.ui.comboBox_2.addItems(name_list)

    def piano_update_midi_files(self, checked: bool):
        self.ui.comboBox_3.clear()
        self.midi_file_list = scan_resources_files("resources", [".mid"])
        name_list = [name for name, _ in self.midi_file_list]
        self.ui.comboBox_3.addItems(name_list)

    def piano_get_preset(self, index: int):
        presets = PianoConfigPresets()
        cfg = None
        match index:
            case -1:
                self.piano_logger.log_error("你未设置钢琴键盘预设!")
                return
            case 0:
                cfg = presets.piano
            case 1:
                cfg = presets.piano_mini
            case 2:
                cfg = presets.piano_vortex
            case 3:
                cfg = presets.piano_large
        return cfg

    def piano_load_preset(self, index: int):
        cfg = self.piano_get_preset(index)
        if cfg is None:
            return
        self.ui.spinBox_4.setValue(cfg.tick_rate)
        self.ui.doubleSpinBox_3.setValue(cfg.base_volume)
        self.ui.doubleSpinBox_2.setValue(cfg.min_volume)
        self.ui.spinBox_5.setValue(cfg.note_dur_extra_ms)
        self.ui.spinBox_6.setValue(cfg.delay_ms)
        self.ui.checkBox.setChecked(cfg.displayer)
        self.ui.lineEdit.setText(cfg.displayer_block)
        self.ui.spinBox.setValue(cfg.displayer_count_left)
        self.ui.spinBox_2.setValue(cfg.displayer_count_right)
        self.ui.spinBox_3.setValue(cfg.displayer_max_moving_tick)
        self.ui.doubleSpinBox.setValue(cfg.displayer_peak_height)
        self.ui.checkBox_2.setChecked(cfg.block_painting)
        self.ui.doubleSpinBox_4.setValue(cfg.motion_y)
        self.ui.doubleSpinBox_5.setValue(cfg.motion_y_random)
        self.ui.spinBox_8.setValue(cfg.painting_base_pos[0])
        self.ui.spinBox_9.setValue(cfg.painting_base_pos[1])
        self.ui.spinBox_10.setValue(cfg.painting_base_pos[2])
        self.ui.spinBox_7.setValue(cfg.block_splits)
        self.ui.checkBox_3.setChecked(cfg.waterfall)
        self.ui.comboBox_3.setCurrentIndex(cfg.waterfall_mode)
        self.ui.spinBox_11.setValue(cfg.waterfall_tick)
        self.ui.doubleSpinBox_6.setValue(cfg.waterfall_height)
        self.ui.lineEdit_3.setText(cfg.waterfall_block)
        self.ui.doubleSpinBox_7.setValue(cfg.waterfall_block_size)
        self.ui.spinBox_12.setValue(cfg.waterfall_block_transition_tick)
        self.ui.checkBox_4.setChecked(cfg.block_painting_use_display_entity)
        self.ui.doubleSpinBox_8.setValue(cfg.displayer_size)

    def on_export_finish(self):
        self.is_exporting = False
        self.ui.pushButton.setEnabled(True)

    def piano_output(self, checked: bool):
        if self.is_exporting:
            self.piano_logger.log_warn("正在导出, 请等待当前任务完成!")
            return

        preset_index = self.ui.comboBox.currentIndex()
        cfg = self.piano_get_preset(preset_index)
        if cfg is None:
            self.piano_logger.log_error(f"无效钢琴键盘预设, 索引: {preset_index}")
            return

        idx_block = self.ui.comboBox_2.currentIndex()
        cfg.block_painting = self.ui.checkBox_2.isChecked()
        if idx_block < 0 and cfg.block_painting:
            self.piano_logger.log_error("请选择方块文件!")
            return
        else:
            cfg.block_path = self.block_file_list[idx_block][1] if idx_block >= 0 else ""

        idx_midi = self.ui.comboBox_3.currentIndex()
        if idx_midi < 0:
            self.piano_logger.log_error("请选择MIDI文件!")
            return
        cfg.midi_path = self.midi_file_list[idx_midi][1]

        cfg.tick_rate = self.ui.spinBox_4.value()
        cfg.base_volume = self.ui.doubleSpinBox_3.value()
        cfg.min_volume = self.ui.doubleSpinBox_2.value()
        cfg.note_dur_extra_ms = self.ui.spinBox_5.value()
        cfg.delay_ms = self.ui.spinBox_6.value()
        cfg.displayer = self.ui.checkBox.isChecked()
        cfg.displayer_block = self.ui.lineEdit.text()
        cfg.displayer_size = self.ui.doubleSpinBox_8.value()
        cfg.displayer_count_left = self.ui.spinBox.value()
        cfg.displayer_count_right = self.ui.spinBox_2.value()
        cfg.displayer_max_moving_tick = self.ui.spinBox_3.value()
        cfg.displayer_peak_height = self.ui.doubleSpinBox.value()
        cfg.motion_y = self.ui.doubleSpinBox_4.value()
        cfg.motion_y_random = self.ui.doubleSpinBox_5.value()
        cfg.painting_base_pos = [
            self.ui.spinBox_8.value(),
            self.ui.spinBox_9.value(),
            self.ui.spinBox_10.value()
        ]
        cfg.block_splits = self.ui.spinBox_7.value()
        cfg.datapack_name = self.ui.lineEdit_2.text()
        if cfg.datapack_name == "":
            self.piano_logger.log_error("数据包名称不能为空!")
            return
        elif " " in cfg.datapack_name:
            self.piano_logger.log_error("数据包名称中不可含有空格!")
            return
        elif bool(re.compile(r'[\u4e00-\u9fff]').search(cfg.datapack_name)):
            self.piano_logger.log_error("数据包名称中不可含有中文!")
            return
        else:
            self.piano_logger.log("\n")
            self.piano_logger.log_info("数据包名称: " + cfg.datapack_name)

        cfg.waterfall = self.ui.checkBox_3.isChecked()
        cfg.waterfall_mode = self.ui.comboBox_3.currentIndex()
        cfg.waterfall_tick = self.ui.spinBox_11.value()
        cfg.waterfall_height = self.ui.doubleSpinBox_6.value()
        cfg.waterfall_block = self.ui.lineEdit_3.text()
        cfg.waterfall_block_size = self.ui.doubleSpinBox_7.value()
        cfg.waterfall_block_transition_tick = self.ui.spinBox_12.value()

        cfg.block_painting_use_display_entity = self.ui.checkBox_4.isChecked()

        self.is_exporting = True
        self.ui.pushButton.setEnabled(False)
        self.piano_logger.log_info(f"生成数据包使用的文件: ")
        if cfg.block_painting:
            self.piano_logger.log_info(f"   方块文件: {cfg.block_path}")
        self.piano_logger.log_info(f"   MIDI文件: {cfg.midi_path}")

        def export_task():
            try:
                piano_main(cfg, self.piano_logger)
            except Exception as e:
                self.piano_logger.log_error(f"导出错误: {str(e)}")
            finally:
                self.export_finish_signal.emit()

        t = threading.Thread(target=export_task)
        t.daemon = True
        t.start()


def main():
    app = QApplication(sys.argv)
    window = VAGWindow()
    window.show()
    app.exec()


if __name__ == '__main__':
    main()
