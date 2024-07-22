"""
Общее ТЗ:
Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать
методы добавления видео, авторизации и регистрации пользователя и т.д.
"""
import time
from time import sleep


class User:
    """
    Каждый объект класса User должен обладать следующими атрибутами и методами:
    Атриубуты: nickname(имя пользователя, строка),
    password(в хэшированном виде, число), age(возраст, число)
    """

    def __init__(self, nickname: str, password: str, age: int):
        self.nickname = nickname
        # функция hash() вызывает метод объекта __hash__(), который установлен по умолчанию для каждого объекта
        self.password = hash(password)
        self.age = age

    # Вернем строку с предполагаемыми атрибутами
    def __str__(self):
        return f'Имя: {self.nickname}, Пароль: {self.password}, Возраст: {self.age}'

    # Сравнение равенства между двумя объектами
    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    # Чтобы сделать класс хэшируемым, он должен
    # реализовать как метод __hash__(self) так и __eq__(self, other)
    def __hash__(self):
        return hash(self.password)

# user = User('Bob', 'qwert1234', 34 )
# print(user)
# user2 = User('John', 'asdf4321', 16)
# print(user2)


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
        self.time_now = time_now
        self.adult_mode = adult_mode

    # Вернем строку с предполагаемыми атрибутами
    def __str__(self):
        return f'Видео: {self.title}'


class UrTube:
    """
    Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
    Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)
    """

    def __init__(self): # иницилизируем атрибуты класса
        # начальные атрибуты класса users, videos пустым списком
        self.users = []
        self.videos = []
        # именованный атрибут класса пустым значением
        self.current_user = None

    def log_in(self, nickname: str, password: str):
        """
        Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти
        пользователя в users с такими же логином и паролем. Если такой пользователь существует,
        то current_user меняется на найденного. Помните, что password передаётся в виде строки,
        а сравнивается по хэшу.
        """
        for i in self.users: # перебираем список с созданным параметром i
            if nickname == i.nickname and password == i.password: # условие: поиск в списке пользователя
                                                                  # с такими же логином и паролем.
                self.current_user = i # пользователь меняется на найденного

    def register(self, nickname: str, password: str, age: int):
        """
        Метод register, который принимает три аргумента: nickname, password, age, и добавляет
        пользователя в список, если пользователя не существует (с таким же nickname). Если существует,
        выводит на экран: "Пользователь {nickname} уже существует". После регистрации,
        вход выполняется автоматически.
        """
        # for i in self.users:
        #     if nickname == i.nickname:
        #         print(f'Пользователь {nickname} уже существует')
        #         break
        #     else:
        #         self.users.append(self.current_user)

        for i in self.users: # перебираем наш список пользователей
            if nickname == i.nickname: # при условии, что пользователь с таким nickname есть в нашем списке
                print(f'Пользователь {nickname} уже существует')
                break
        self.current_user = User(nickname, password, age) # текущий пользователь None(не был создан), мы его определяем
        self.users.append(self.current_user) # и добавляем в список пользоваелей

    def log_out(self):
        """
        Метод log_out для сброса текущего пользователя на None.
        """
        self.current_user = None

    def add(self, *args): # *args произвольное число позиционных параметров
        """
        Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos,
        если с таким же названием видео ещё не существует. В противном случае ничего не происходит.
        """
        for i in args: # перебираем список *args объектов класса Video
            for j in self.videos: # перебираем наш список объектов класса UrTube
                if i.title in j.title: # условие: если есть имя (из класса Video) из списка *args в нашем списке
                    break # оставляем как есть
            else:
                self.videos.append(i) # иначе добавляем объект из *args в наш список

        # for title in args:
        #     self.videos.append(title)

    def get_videos(self, control_word):
        """
        Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео,
        содержащих поисковое слово. Следует учесть, что слово 'UrbaN' присутствует в строке
        'Urban the best' (не учитывать регистр).
        """
        result = [] # переменная с пустым списком, для возврата списка с результатом работы функции
        for i in self.videos: # перебираем наш список с видео
            if control_word.lower() in i.title.lower(): # условие переборки: поисковое слово с нижним регистром
                result.append(i.title) # добавляем название видео в созданный заранее список
        return result

        # list_ = []
        # for i in self.videos:
        #     if control_word.upper() in i.title.upper():
        #         list_.append(i.title)
        # return list_

    def watch_video(self, title: str):
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
        for i in self.users:
            if i != self.current_user:
                print('Войдите в аккаунт, чтобы смотреть видео')
        for video in self.videos:
            if title != video.title:
                continue
            if video.adult_mode < 18:
                print('Вам нет 18 лет, пожалуйста покиньте страницу')
                break
            else:
                for time_now in video.duration:
                    time.sleep(1)
                    time_now += 1
                    print(video.time_now)
            def watch_video(self, movie):
        if not self.current_user:
            print("Войдите в аккаунт, чтобы смотреть видео.")
            return
        for selected_video in self.videos:
            if selected_video.title == movie:
                if selected_video.adult_mode and self.current_user.age < 18:
                    print("Вам нет 18-ти лет, пожалуйста, покиньте страницу!")
                    return

                for i in range(selected_video.duration):
                    p
for i in range(selected_video.duration):
                    print(f"{i+1}", end = ' ')
                    sleep(1)
                    selected_video.time_now += 1

                selected_video.time_now = 0
                print("конец видео")
                sleep(3)
from time import sleep




ur = UrTube()
v1 = Video('Лучший язык программирования 2024 года', 200)
v2 = Video('Для чего девушкам парень программист?', 10, adult_mode=True)

# Добавление видео
ur.add(v1, v2)

# Проверка поиска
print(ur.get_videos('лучший'))
print(ur.get_videos('ПРОГ'))

# Проверка на вход пользователя и возрастное ограничение
ur.watch_video('Для чего девушкам парень программист?')
ur.register('vasya_pupkin', 'lolkekcheburek', 13)
ur.watch_video('Для чего девушкам парень программист?')
ur.register('urban_pythonist', 'iScX4vIJClb9YQavjAgF', 25)
ur.watch_video('Для чего девушкам парень программист?')

# Проверка входа в другой аккаунт
ur.register('vasya_pupkin', 'F8098FM8fjm9jmi', 55)
print(ur.current_user)

# Попытка воспроизведения несуществующего видео
ur.watch_video('Лучший язык программирования 2024 года!')
