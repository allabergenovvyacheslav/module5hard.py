"""
Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать
методы добавления видео, авторизации и регистрации пользователя и т.д.
"""

from time import sleep


class User:
    """
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка),
    password(в хэшированном виде, число), age(возраст, число)
    """

    def __init__(self, nickname: str, password: int, age: int):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Имя: {self.nickname}, Пароль: {self.password}, Возраст: {self.age}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    def __hash__(self):
        return hash(self.password)


class Video:
    """
    Каждый объект класса Video должен обладать следующими атрибутами и методами:
    Атриубуты: title(заголовок, строка), duration(продолжительность, секунды),
    time_now(секунда остановки (изначально 0)), adult_mode(ограничение по возрасту,
    bool (False по умолчанию))
    """

    def __init__(self, title: str, duration: int, time_now: int = 0, adult_mode: bool = False):
        self.title = title
        self.duration = duration
        self.time_now = 0
        self.adult_mode = adult_mode


class UrTube:
    """
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
    """

    def __init__(self):
        self.users = []
        self.video = []
        self.current_user = None

    def log_in(self, nickname, password):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти
        пользователя в users с такими же логином и паролем. Если такой пользователь существует,
        то current_user меняется на найденного. Помните, что password передаётся в виде строки,
        а сравнивается по хэшу.
        """
        pass

    def register(self, nickname, password, age):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет
        пользователя в список, если пользователя не существует (с таким же nickname). Если существует,
        выводит на экран: "Пользователь {nickname} уже существует". После регистрации,
        вход выполняется автоматически.
        """
        pass

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        pass

    def add(self, *args):
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        """
        pass

    def get_videos(self, control_word):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
        'Urban the best' (не учитывать регистр).
        """
        pass

    def watch_video(self):
        """
        Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
        то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
        После текущее время просмотра данного видео сбрасывается.
        """
        """
        Для метода watch_video так же учитывайте следующие особенности:
        1. Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
        2. Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить 
        в консоль надпись: "Войдите в аккаунт, чтобы смотреть видео"
        3. Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, 
        т.к. есть ограничения 18+. Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
        После воспроизведения нужно выводить: "Конец видео"
        """
        pass



#ur = UrTube()
#v1 = Video('Лучший язык программирования 2024 года', 200)
#v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)
#
## Добавление видео
#ur.add(v1, v2)
#
## Проверка поиска
#print(ur.get_videos('лучший'))
#print(ur.get_videos('ПРОГ'))
#
## Проверка на вход пользователя и возрастное ограничение
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('vasya_pupkin', 'lolkekcheburek', 13)
#ur.watch_video('Для чего девушкам парень программист?')
#ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
#ur.watch_video('Для чего девушкам парень программист?')
#
## Проверка входа в другой аккаунт
#ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
#print(ur.current_user)
#
## Попытка воспроизведения несуществующего видео
#ur.watch_video('Лучший язык программирования 2024 года!')