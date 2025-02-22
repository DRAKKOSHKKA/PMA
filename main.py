import sys
import os
from backoff import expo
from colorama import init, Fore
init(autoreset=True)
os.system('title Python Music App')

VERSION = '1.0.1'
DEVELOPERS = {'DRAKKOSHKKA': 't.me/drakkoshkka'}
PATH_LOGS = f'{os.path.dirname(__file__)}\\logs'
GLOBAL_MUSIC_FOLDER = f'{os.path.dirname(__file__)}\\sounds'
SOUNDS_SELECTED = 'input.wav'
DEBUG_MODE = False
_LOG_FILE = []

def sound_covert():
    AddLog('[sound_covert] Использован конвертер звука')
    from pydub import AudioSegment
    from tkinter import filedialog as tkf

    sound = tkf.askopenfilename(title="Выберите MP3 файл", filetypes=[("MP3 files", "*.mp3")])

    if sound:
        sound_name = sound.split('/')[len(sound.split('/')) - 1][:-4]

        audio = AudioSegment.from_mp3(sound)
        print('Ковертация звука...')
        AddLog(f'[sound_covert] Начало конвертации')
        audio.export(f'{GLOBAL_MUSIC_FOLDER}\\{sound_name}.wav', format="wav")
        AddLog(f'[sound_covert] Конвертирован {sound} в {GLOBAL_MUSIC_FOLDER}\\{sound_name}.wav')
    else:
        AddWarn('[sound_covert] Отмена выбора')
        os.system('cls')
        print(Fore.RED + 'Вы отменили выбор!\n')
        input('Нажмите клашиву ENTER...')
        os.system('cls')
        run_code()

def AddError(text):
    import datetime
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    current_time = now.strftime("%H:%M:%S")

    global _LOG_FILE
    _LOG_FILE.append(Fore.RED + f'[{current_time}][ERROR] -> {text}')

def AddWarn(text):
    import datetime
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    current_time = now.strftime("%H:%M:%S")

    global _LOG_FILE
    _LOG_FILE.append(Fore.YELLOW + f'[{current_time}][WARN] -> {text}')

def AddLog(text):
    import datetime
    now = datetime.datetime.now()
    hour = now.hour
    minute = now.minute
    second = now.second
    current_time = now.strftime("%H:%M:%S")

    global _LOG_FILE
    _LOG_FILE.append(Fore.LIGHTCYAN_EX + f'[{current_time}][LOGS] -> {text}')

def run_code():
    while True:
        if DEBUG_MODE:
            print(Fore.LIGHTBLUE_EX + 'Включен режим разработчика')
            print(Fore.LIGHTBLUE_EX + 'Вам доступны расширенные функции откладки.\n')
        print(f'Рабочий файл: "{GLOBAL_MUSIC_FOLDER}\\{SOUNDS_SELECTED}"')
        print('Выберите действие:')
        print('[1] Спектограмма')
        print('[2] Осцилограмма')
        print('[3] Конвертер звука (mp3 > wav)')
        print('[4] Узнать данные звукового файла')
        print('[5] Изменить параметры звукового файла')
        print('[6] Настройки')
        print('[7] О проекте')
        if DEBUG_MODE:
            print('------------------')
            print('[8] Список логов')
            print('[9] Экспорт логов')
        x = input('>')
        if x == '1':
            AddLog('[main] Переход в спектограмму')
            os.system('cls')
            print('Ожидайте, происходит анализ звукового файла...')
            run_code_spector()
            os.system('cls')
        elif x == '2':
            AddLog('[main] Переход в осцилограмму')
            os.system('cls')
            print('Ожидайте, происходит анализ звукового файла...')
            run_code_osc()
            os.system('cls')
        elif x == '3':
            AddLog('[main] Переход в конвертер')
            os.system('cls')
            print('Выберите файл с раширением *.mp3')
            sound_covert()
            os.system('cls')
            print('Аудио файл был успешно конвертирован.')
            print(f'Он был перенесён в главную папку ({GLOBAL_MUSIC_FOLDER})')
            input('Нажмите клашиву ENTER...')
            os.system('cls')
        elif x == '4':
            AddLog('[main] Переход в анализатор')
            os.system('cls')
            print('Происходит нализ...')
            _temp = get_wav_info(f'{GLOBAL_MUSIC_FOLDER}\\{SOUNDS_SELECTED}')
            if _temp != None:
                print('Полученные данные:')
                print(f'Каналы: {_temp["channels"]}')
                print(f'Длина: {_temp["length_ms"]}')
                print(f'Частота: {_temp["frame_rate"]}')
                print(f'BPM: ~{round(_temp["bpm"])}')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
            else:
                AddWarn('[main][analuz] Ошибка извлечения')
                os.system('cls')
                print(Fore.RED + 'Не удалось извлечь данные из аудиофайла!\n')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
        elif x == '5':
            AddLog('[main] Переход в изменитель звукового файла')
            os.system('cls')
            change_music()
        elif x == '6':
            AddLog('[main] Переход в настройки')
            os.system('cls')
            settings()
        elif x == '7':
            AddLog('[main] Переход информация о проекте')
            os.system('cls')
            get_developers()
        elif x == '8':
            AddLog('[main] Переход в логи')
            if DEBUG_MODE:
                _count = 0
                os.system('cls')
                print('Список логов:\n')
                for i in _LOG_FILE:
                    _count += 1
                    print(f'[{_count}]{i}')
                input('\nНажмите клашиву ENTER...')
                os.system('cls')
            else:
                os.system('cls')
                print(Fore.RED + 'Вы ввели не верный вариант!\n')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
        elif x == '9':
            AddLog('[main] Экспорт логов...')
            if DEBUG_MODE:
                os.system('cls')
                export_logs()
                print('Логи были успешно экспортированны!')
                print(f'Местоположение логов: {PATH_LOGS}')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
            else:
                os.system('cls')
                print(Fore.RED + 'Вы ввели не верный вариант!\n')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
        else:
            AddWarn('[main] Неверный ввод данных')
            os.system('cls')
            print(Fore.RED + 'Вы ввели не верный вариант!\n')
            input('Нажмите клашиву ENTER...')
            os.system('cls')

def get_developers():
    print('Название проекта: Python Music App (PMA)\n')
    print('Описание проекта:')
    print('Это приложение позволяет анализировать и изменять аудиофайлы в формате WAV. ')
    print('Оно предоставляет функциональность для просмотра спектрограммы и осциллограммы звука,')
    print('конвертации MP3 файлов в WAV, получения информации о файле, изменения параметров звука')
    print('и выбора активного звукового файла для работы.\n')
    print(f'Версия приложения: v{VERSION}\n')
    print('Разработчики:')
    _count = 0
    for i in DEVELOPERS:
        _count += 1
        print(f'[{_count}] {i} -> {DEVELOPERS[i]}')
    input('\nНажмите клашиву ENTER...')
    os.system('cls')

def export_logs():
    import datetime, re
    now = datetime.datetime.now()
    current_time = now.strftime("%d-%H-%M-%S")
    path = f'{PATH_LOGS}\\{current_time}.txt'

    with open(path, "w", encoding="utf-8") as file:
        for i in _LOG_FILE:
            file.write(re.sub(r'[\n\t\r\f\v]', '', i) + "\n")

def _get_files(folder, nm) -> list:
    AddLog('[_get_files] получение данных файла')
    files_with_extension = []
    for filename in os.listdir(folder):
        if filename.endswith(nm):
            files_with_extension.append(filename)
    return files_with_extension

def change_music():
    ton = 1
    speed = 1
    while True:
        print(f'Выбранный файл: "~/sounds/{SOUNDS_SELECTED}"')
        print(f'Скорость: x{speed}')
        print(f'Тональность: x{ton}')
        print('--------------------')
        print('Выберите действие:')
        print('[0] Назад')
        print('[1] Изменить скорость')
        print('[2] Изменить тональность')
        print('[3] Сохранить')
        x = input('>')
        if x == '0':
            AddLog('[change_music] Переход назад')
            os.system('cls')
            run_code()
        if x == '1':
            AddLog('[change_music][speed] Изменение скорости')
            os.system('cls')
            print('Задайте новую скорость (от 0.5 до 5):')
            x = input('>')
            if check(x):
                if 0.5 <= float(x) and float(x) <= 5:
                    AddLog(f'[change_music][speed] Новое значение переменной - {x}')
                    speed = float(x)
                    os.system('cls')
                else:
                    AddWarn(f'[change_music][speed][2] Неверное значение')
                    os.system('cls')
                    print(Fore.RED + 'Ваше значение не соответствует требованиям!')
                    input('Нажмите клашиву ENTER...')
                    os.system('cls')
            else:
                AddWarn(f'[change_music][speed][1] Неверное значение')
                os.system('cls')
                print(Fore.RED + 'Вы ввели не верные параметры!')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
        elif x == '2':
            AddLog(f'[change_music][ton] Изменение тональности')
            os.system('cls')
            print('Задайте новую тональность (от 0.5 до 5):')
            x = input('>')
            if check(x):
                if 0.5 <= float(x) and float(x) <= 5:
                    AddLog(f'[change_music][ton] Новое значение переменной - {x}')
                    ton = float(x)
                    os.system('cls')
                else:
                    AddWarn(f'[change_music][ton][2] Неверное значение')
                    os.system('cls')
                    print(Fore.RED + 'Ваше значение не соответствует требованиям!')
                    input('Нажмите клашиву ENTER...')
                    os.system('cls')
            else:
                AddWarn(f'[change_music][ton][1] Неверное значение')
                os.system('cls')
                print(Fore.RED + 'Вы ввели не верные параметры!')
                input('Нажмите клашиву ENTER...')
                os.system('cls')
        elif x == '3':
            AddLog(f'[change_music] Применение изменений')
            change_speed_and_pitch(f'{GLOBAL_MUSIC_FOLDER}\\{SOUNDS_SELECTED}', speed, ton)
            os.system('cls')
            print(Fore.GREEN + 'Файл был успешно изменён и сохранён!')
            AddLog(f'[change_music] Успешное сохранение')
            input('Нажмите клашиву ENTER...')
            os.system('cls')
            run_code()
        else:
            AddWarn(f'[change_music] Неверное значение')
            os.system('cls')
            print(Fore.RED + 'Вы ввели не верное значение!\n')
            input('Нажмите клашиву ENTER...')
            os.system('cls')

def check(num):
    import re
    AddLog(f'[check] Начало проверки -> {num}')
    pattern = r"^[-+]?(\d*\.\d+|\d+\.\d*|\d+)$"
    x = bool(re.match(pattern, num))
    if x:
        AddLog(f'[check] Успешно')
    else:
        AddWarn(f'[check] Ошибка')
    return x

def settings():
    global SOUNDS_SELECTED
    while True:
        _count = 0
        print('Выберите звуковой файл (папка ./sounds):')
        print('[0] Назад')
        for i in _get_files(GLOBAL_MUSIC_FOLDER, '.wav'):
            _count += 1
            print(f'[{_count}] {i}')

        x = input('>')
        if x.isdigit():
            if 0 <= int(x) and int(x) <= _count:
                if int(x) == 0:
                    AddLog(f'[settings] Выбранно назад')
                    os.system('cls')
                    run_code()
                else:
                    SOUNDS_SELECTED = _get_files(GLOBAL_MUSIC_FOLDER, '.wav')[int(x) - 1]
                    AddLog(f'[settings] Выбран файл {x} - {SOUNDS_SELECTED}')
                    os.system('cls')
                    run_code()
        AddWarn(f'[settings] Не верное значение')
        os.system('cls')
        print(Fore.RED + 'Вы ввели не верное значение!\n')
        input('Нажмите клашиву ENTER...')
        os.system('cls')

def run_code_osc():
    AddLog(f'[run_code_osc] Начало кода...')
    from pydub import AudioSegment
    import numpy as np
    import matplotlib.pyplot as plt

    # Загружаем аудиофайл
    audio = AudioSegment.from_file(f'{GLOBAL_MUSIC_FOLDER}\\{SOUNDS_SELECTED}')

    # Преобразуем данные в массив NumPy
    samples = np.array(audio.get_array_of_samples())
    frame_rate = audio.frame_rate

    # Создаем временной массив для осциллограммы
    time = np.linspace(0, len(samples) / frame_rate, num=len(samples))

    AddLog(f'[run_code_osc] Успешная обработка')
    # Визуализируем осциллограмму
    plt.figure(figsize=(12, 6))
    plt.plot(time, samples)
    plt.title('Осцилограмма звукового файла')
    plt.xlabel('Время [с]')
    plt.ylabel('Амплитуда')
    plt.grid()
    AddLog(f'[run_code_osc] Начало отображения...')
    plt.show()
    AddLog(f'[run_code_osc] Конец кода')

def change_speed_and_pitch(input_file, speed_factor=1.0, pitch_shift=0):
    AddLog(f'[change_speed_and_pitch] Начало работы')
    from pydub import AudioSegment
    audio = AudioSegment.from_file(input_file)

    # Изменение скорости
    new_sample_rate = int(audio.frame_rate * speed_factor)
    speed_changed_audio = audio._spawn(audio.raw_data, overrides={'frame_rate': new_sample_rate})

    # Изменение тональности
    if pitch_shift != 0:
        # Изменение тональности с помощью метода shift
        pitch_changed_audio = speed_changed_audio._spawn(speed_changed_audio.raw_data, overrides={
            'frame_rate': int(new_sample_rate * (2 ** (pitch_shift / 12.0)))
        })
    else:
        pitch_changed_audio = speed_changed_audio

    # Сохранение результата
    pitch_changed_audio.export(f'{input_file[:-4]}-new.wav', format="wav")
    AddLog(f'[change_speed_and_pitch] Сохранение файла из {input_file} в {input_file[:-4]}-new.wav / С праметрами: speed={speed_factor} ton={pitch_shift}')

def get_bpm(file_path):
    AddLog(f'[get_bpm] Начало кода...')
    from pydub import AudioSegment
    import numpy as np
    from scipy.signal import find_peaks
    audio = AudioSegment.from_file(file_path)
    samples = np.array(audio.get_array_of_samples())
    if audio.channels == 2:
        samples = samples[::2]
    samples = samples / np.max(np.abs(samples))
    amplitude = np.abs(samples)
    peaks, _ = find_peaks(amplitude, height=0.01, distance=1000)
    bpm = (len(peaks) / (len(samples) / audio.frame_rate)) * 10

    AddLog(f'[get_bpm] Выходная сумма: {bpm}')
    return bpm

def get_wav_info(file_path):
    AddLog(f'[get_wav_info] Начало кода')
    import wave
    from pydub import AudioSegment
    import numpy as np
    from scipy.signal import find_peaks
    os.system('cls')
    try:
        AddLog(f'[get_wav_info] Попытка раскодировки методом wave...')
        # Попытка открыть файл с помощью wave
        with wave.open(file_path, 'rb') as wav_file:
            AddLog(f'[get_wav_info][wave] Успешно!')
            params = wav_file.getparams()
            bpm = get_bpm(file_path)
            info = {
                'channels': params.nchannels,
                'sample_width': params.sampwidth,
                'frame_rate': params.framerate,
                'frame_count': params.nframes,
                'bpm': bpm,
                'length_ms': (params.nframes / params.framerate) * 1000  # длина в миллисекундах
            }
            return info

    except wave.Error as e:
        AddWarn(f'[get_wav_info] Раскодировать не удалось')
        print(Fore.RED + 'Не удалось получить данные файла при помощи стандартных методов!')
        print(Fore.RED + f"Текст ошибки: {e}")
        print(Fore.RED + 'Вы можете узнать подробнее в документации README')
        print(Fore.GREEN + "Попытка открыть файл с помощью сторонних библиотек...\n")

        # Если не удалось открыть, используем Pydub
        try:
            AddLog(f'[get_wav_info] Попытка раскодировки PyDub')
            audio = AudioSegment.from_file(file_path)
            bpm = get_bpm(file_path)
            info = {
                'channels': audio.channels,
                'sample_width': audio.sample_width,
                'frame_rate': audio.frame_rate,
                'length_ms': len(audio),
                'bpm': bpm,
                'frame_count': audio.frame_count(),
            }
            AddLog(f'[get_wav_info] Успешно!')
            return info

        except Exception as e:
            AddError(f'[get_wav_info] Ошибка')
            print(Fore.RED + "Ошибка при открытии файла с помощью сторонних библиотек!")
            print(Fore.RED + f"Текст ошибки: {e}\n")
            return None

def run_code_spector():
    AddLog(f'[run_code_spector] Начало кода')
    from pydub import AudioSegment
    import numpy as np
    import matplotlib.pyplot as plt
    import scipy.signal

    # Конвертируем файл в WAV с помощью pydub
    audio = AudioSegment.from_file(f'{GLOBAL_MUSIC_FOLDER}\\{SOUNDS_SELECTED}')
    samples = np.array(audio.get_array_of_samples())
    frame_rate = audio.frame_rate

    # Создаем спектрограмму
    frequencies, times, Sxx = scipy.signal.spectrogram(samples, fs=frame_rate)

    # Визуализируем спектрограмму
    AddLog(f'[run_code_spector] Начало plt')
    plt.figure(figsize=(10, 6))
    plt.pcolormesh(times, frequencies, 10 * np.log10(Sxx), shading='gouraud')
    plt.ylabel('Частота [Гц]')
    plt.xlabel('Время [с]')
    plt.title('Спектрограмма аудиофайла')
    plt.colorbar(label='Интенсивность [дБ]')
    plt.ylim(0, 20000)  # Ограничиваем частоты до 20 кГц
    AddLog(f'[run_code_spector] Начало отображения')
    plt.show()
    AddLog(f'[run_code_spector] Конец кода')

AddLog(f'Начало проверки на аргументы...')
if sys.argv[len(sys.argv) - 1] != None:
    s = sys.argv[len(sys.argv) - 1]
else:
    s = ''
if s == '--show-error':
    os.system('title Python Music App + Debug')
    DEBUG_MODE = True
    AddLog('Запущен исполняемый файл в режиме разработчика')
    run_code()
else:
    try:
        run_code()
    except ModuleNotFoundError as e:
        print(Fore.RED + f'Вы не установили нужные модули!')
        print(Fore.RED + f'Прочитайте документацию README.txt')
        print(Fore.RED + f'Текст ошибки: {e}')
        input('\nНажмите клашиву ENTER...')
        exit()
    except Exception as e:
        print(Fore.RED + f'Произошла критическая ошибка!')
        print(Fore.RED + f'Попробуйте прочитать документацию README.txt')
        print(Fore.RED + f'Данная ошибка не была предусмотрена, поэтому решения в документации может не быть!')
        print(Fore.RED + f'Текст ошибки: {e}')
        input('\nНажмите клашиву ENTER...')
        exit()
