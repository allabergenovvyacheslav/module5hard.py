import time

# Общее ТЗ:
# Реализовать классы для взаимодействия с платформой, каждый из которых будет содержать методы добавления видео,
# авторизации и регистрации пользователя и т.д.
#
# Подробное ТЗ:
#
# Каждый объект класса User должен обладать следующими атрибутами и методами:
# Атриубуты: nickname(имя пользователя, строка), password(в хэшированном виде, число), age(возраст, число)

# Каждый объект класса Video должен обладать следующими атрибутами и методами:
# Атриубуты: title(заголовок, строка), duration(продолжительность, секунды), time_now(секунда остановки (изначально 0)),
# adult_mode(ограничение по возрасту, bool (False по умолчанию))

# Каждый объект класса UrTube должен обладать следующими атрибутами и методами:
#  Атриубты: users(список объектов User), videos(список объектов Video), current_user(текущий пользователь, User)

# Метод log_in, который принимает на вход аргументы: nickname, password и пытается найти пользователя в users с
# такими же логином и паролем. Если такой пользователь существует, то current_user меняется на найденного. Помните,
# что password передаётся в виде строки, а сравнивается по хэшу.

# Метод register, который принимает три аргумента: nickname, password, age, и добавляет пользователя в список, если
# пользователя не существует (с таким же nickname). Если существует, выводит на экран: "Пользователь {nickname} уже
# существует". После регистрации, вход выполняется автоматически.

# Метод log_out для сброса текущего пользователя на None.

# Метод add, который принимает неограниченное кол-во объектов класса Video и все добавляет в videos, если с таким же
# названием видео ещё не существует. В противном случае ничего не происходит.

# Метод get_videos, который принимает поисковое слово и возвращает список названий всех видео, содержащих поисковое
# слово. Следует учесть, что слово 'UrbaN' присутствует в строке 'Urban the best' (не учитывать регистр).

# Метод watch_video, который принимает название фильма, если не находит точного совпадения(вплоть до пробела),
# то ничего не воспроизводится, если же находит - ведётся отчёт в консоль на какой секунде ведётся просмотр.
# После текущее время просмотра данного видео сбрасывается.

# Для метода watch_video так же учитывайте следующие особенности:
# Для паузы между выводами секунд воспроизведения можно использовать функцию sleep из модуля time.
# Воспроизводить видео можно только тогда, когда пользователь вошёл в UrTube. В противном случае выводить в консоль
# надпись: "Войдите в аккаунт, чтобы смотреть видео"
# Если видео найдено, следует учесть, что пользователю может быть отказано в просмотре, т.к. есть ограничения 18+.
# Должно выводиться сообщение: "Вам нет 18 лет, пожалуйста покиньте страницу"
# После воспроизведения нужно выводить: "Конец видео"


class User:

    def __init__(self, nickname, password, age):
        self.nickname = nickname
        self.password = hash(password)
        self.age = age

    def __str__(self):
        return f'Имя: {self.nickname}'

    def __eq__(self, other):
        return self.nickname == other.nickname and self.password == other.password

    # Чтобы сделать класс хэшируемым, он должен
    # реализовать как метод __hash__(self) так и __eq__(self, other)
    def __hash__(self):
        return hash(self.password)

# u1 = User('Bob', 'qwerty12345', 32)
# print(u1)
class Video:

    def __init__(self, title, duration, time_now=0, adult_mode=False):
        self.title = title
        self.duration = duration
        self.time_now = time_now
        self.adult_mode = adult_mode

    def __str__(self):
        return f'Видео: {self.title}'

class UrTube:

    def __init__(self, current_user=None):
        self.users = []
        self.videos = []
        self.current_user = current_user

    def log_in(self, nickname, password):
        for user in self.users:
            if nickname == user.nickname and password == user.password:
                self.current_user = user
            else:
                print('Такой пользователь не зарегистрирован')
    def register(self, nickname, password, age):
        for user in self.users:
            if user.nickname == nickname:
                print(f'Пользователь {nickname} уже существует')
                return
        user = User(nickname, password, age)
        self.current_user = user
        self.users.append(user)


    def log_out(self):
        self.current_user = None

    def add(self, *args):
        for i in args:
            if i not in self.videos:
                self.videos.append(i)

    def get_videos(self, control_word):
        result = []
        for i in self.videos:
            if control_word.lower() in i.title.lower():
                result.append(i.title)
        return result

    def watch_video(self, film_name):
        if self.current_user not in self.users:
            print('Войдите в аккаунт, чтобы смотреть видео')
            return self
        for video in self.videos:
            if video.title == film_name:
                if video.adult_mode and self.current_user.age < 18:
                    print('Вам нет 18 лет, пожалуйста покиньте страницу')
                    return self
                for i in range(int(video.duration)):
                    print(f'{i + 1}', end=' ')
                    time.sleep(1)
                i += 1
                print('Конец видео')


if __name__ == '__main__':

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
