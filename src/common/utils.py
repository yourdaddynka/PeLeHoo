def get_path_upload_track(instance, file):
    """ Построение пути к файлу, format: (media)/track/album/audio.mp3
    """
    return f'track/{instance.album}/{file}'
