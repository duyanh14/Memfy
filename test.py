import sys
from PyQt5 import QtWidgets as qtw
from PyQt5 import QtGui as qtg
from PyQt5 import QtCore as qtc
from PyQt5 import QtChart as qtch

from collections import deque
import psutil



class CPUUsageView(qtch.QChartView):

    num_data_points = 500
    chart_title = "CPU Utilization"

    def __init__(self):
        super().__init__()

        # create chart
        chart = qtch.QChart(title=self.chart_title)
        self.setChart(chart)

        # series
        self.series = qtch.QSplineSeries(name="Percentage")
        chart.addSeries(self.series)

        # Create data container
        self.data = deque(
            [0] * self.num_data_points, maxlen=self.num_data_points)
        self.series.append([
            qtc.QPoint(x, y)
            for x, y in enumerate(self.data)
        ])

        # CPU Axes
        x_axis = qtch.QValueAxis()
        x_axis.setRange(0, self.num_data_points)
        x_axis.setLabelsVisible(False)
        y_axis = qtch.QValueAxis()
        y_axis.setRange(0, 100)
        chart.setAxisX(x_axis, self.series)
        chart.setAxisY(y_axis, self.series)

        # Appearance tweaks
        self.setRenderHint(qtg.QPainter.Antialiasing)

        # configure timer
        self.timer = qtc.QTimer(
            interval=200, timeout=self.refresh_stats)
        self.timer.start()

    def refresh_stats(self):
        usage = psutil.cpu_percent()
        self.data.append(usage)
        new_data = [
            qtc.QPoint(x, y)
            for x, y in enumerate(self.data)]
        self.series.replace(new_data)

    def keyPressEvent(self, event):
        keymap = {
            qtc.Qt.Key_Up: lambda: self.chart().scroll(0, -10),
            qtc.Qt.Key_Down: lambda: self.chart().scroll(0, 10),
            qtc.Qt.Key_Right: lambda: self.chart().scroll(-10, 0),
            qtc.Qt.Key_Left: lambda: self.chart().scroll(10, 0),
            qtc.Qt.Key_Greater: self.chart().zoomIn,
            qtc.Qt.Key_Less: self.chart().zoomOut,
        }
        callback = keymap.get(event.key())
        if callback:
            callback()



class MainWindow(qtw.QMainWindow):

    def __init__(self):
        """MainWindow constructor.
        This widget will be our main window.
        We'll define all the UI components in here.
        """
        super().__init__()
        # Main UI code goes here
        tabs = qtw.QTabWidget()
        self.setCentralWidget(tabs)



        #############################
        # CPU usage as a line chart #
        #############################

        cpu_view = CPUUsageView()
        tabs.addTab(cpu_view, "CPU Usage")



        # End main UI code
        self.show()



if __name__ == '__main__':
    app = qtw.QApplication(sys.argv)
    # it's required to save a reference to MainWindow.
    # if it goes out of scope, it will be destroyed.
    mw = MainWindow()
    sys.exit(app.exec())