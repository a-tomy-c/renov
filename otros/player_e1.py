import sys
from PySide6.QtWidgets import (QApplication, QMainWindow, QVBoxLayout, 
                               QHBoxLayout, QWidget, QPushButton, 
                               QSlider, QLabel, QFileDialog)
from PySide6.QtMultimedia import QMediaPlayer, QAudioOutput
from PySide6.QtMultimediaWidgets import QVideoWidget
from PySide6.QtCore import Qt, QUrl

class VideoPlayer(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("Video Player")
        self.setGeometry(100, 100, 800, 600)
        
        # Crear el widget central
        central_widget = QWidget()
        self.setCentralWidget(central_widget)
        
        # Layout principal
        layout = QVBoxLayout(central_widget)
        
        # Widget de video
        self.video_widget = QVideoWidget()
        layout.addWidget(self.video_widget)
        
        # Crear el reproductor multimedia
        self.media_player = QMediaPlayer()
        self.audio_output = QAudioOutput()
        self.media_player.setAudioOutput(self.audio_output)
        self.media_player.setVideoOutput(self.video_widget)
        
        # Controles
        controls_layout = QHBoxLayout()
        
        # Botón abrir archivo
        self.open_button = QPushButton("Abrir Video")
        self.open_button.clicked.connect(self.open_file)
        controls_layout.addWidget(self.open_button)
        
        # Botón play/pause
        self.play_button = QPushButton("Play")
        self.play_button.clicked.connect(self.play_pause)
        controls_layout.addWidget(self.play_button)
        
        # Botón stop
        self.stop_button = QPushButton("Stop")
        self.stop_button.clicked.connect(self.stop)
        controls_layout.addWidget(self.stop_button)
        
        # Slider de posición
        self.position_slider = QSlider(Qt.Horizontal)
        self.position_slider.sliderMoved.connect(self.set_position)
        controls_layout.addWidget(self.position_slider)
        
        # Label de tiempo
        self.time_label = QLabel("00:00 / 00:00")
        controls_layout.addWidget(self.time_label)
        
        # Slider de volumen
        self.volume_slider = QSlider(Qt.Horizontal)
        self.volume_slider.setRange(0, 100)
        self.volume_slider.setValue(50)
        self.volume_slider.setMaximumWidth(100)
        self.volume_slider.valueChanged.connect(self.set_volume)
        controls_layout.addWidget(QLabel("Vol:"))
        controls_layout.addWidget(self.volume_slider)
        
        layout.addLayout(controls_layout)
        
        # Conectar señales
        self.media_player.positionChanged.connect(self.position_changed)
        self.media_player.durationChanged.connect(self.duration_changed)
        self.media_player.playbackStateChanged.connect(self.state_changed)
        
        # Establecer volumen inicial
        self.set_volume(50)
    
    def open_file(self):
        file_path, _ = QFileDialog.getOpenFileName(
            self, "Abrir Video", "", 
            "Video Files (*.mp4 *.avi *.mkv *.mov *.wmv);;All Files (*)"
        )
        
        if file_path:
            self.media_player.setSource(QUrl.fromLocalFile(file_path))
            self.play_button.setText("Play")
    
    def play_pause(self):
        if self.media_player.playbackState() == QMediaPlayer.PlayingState:
            self.media_player.pause()
        else:
            self.media_player.play()
    
    def stop(self):
        self.media_player.stop()
    
    def set_position(self, position):
        self.media_player.setPosition(position)
    
    def set_volume(self, volume):
        self.audio_output.setVolume(volume / 100.0)
    
    def position_changed(self, position):
        self.position_slider.setValue(position)
        self.update_time_label()
    
    def duration_changed(self, duration):
        self.position_slider.setRange(0, duration)
        self.update_time_label()
    
    def state_changed(self, state):
        if state == QMediaPlayer.PlayingState:
            self.play_button.setText("Pause")
        else:
            self.play_button.setText("Play")
    
    def update_time_label(self):
        position = self.media_player.position()
        duration = self.media_player.duration()
        
        pos_time = self.format_time(position)
        dur_time = self.format_time(duration)
        
        self.time_label.setText(f"{pos_time} / {dur_time}")
    
    def format_time(self, ms):
        seconds = ms // 1000
        minutes = seconds // 60
        seconds = seconds % 60
        return f"{minutes:02d}:{seconds:02d}"

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    player = VideoPlayer()
    player.show()
    
    sys.exit(app.exec())