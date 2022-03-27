# Antivirus
Программное обеспечение (далее ПО) – это комплекс из отдельных про-грамм, которые объединены друг с другом для достижения общего ре-зультата.
Наличие ПО - это одно из обязательных условий работоспособности практически всех современных информационных систем, наряду с аппа-ратным обеспечением и информационными ресурсами. ПО является одной из составляющих частей компьютера. Современное ПО представляет собой модули, которые объединены в единую систему и дополняют друг друга. Модули взаимодействуют друг с другом через запрограммированный алгоритм. ПО принято разделять на три группы:
1. Системное;
2. Прикладное;
3. Инструментальное.
Программное обеспечение, которое я разрабатываю относится к группе «Системное». Рассмотри по подробнее:
Цель проекта.
Цель проекта – разработать систему обеспечения защиты информации (далее Система). В Системе должна быть предусмотрена защита системы, на которой она установлена, взаимодействие с базой данных.
Описание системы.
Система состоит из пакетов, в которых находятся модули, содержащие в себе функциональные блоки. Всего в программе четыре пакета:
1. Antivirus package;
2. Database package;
3. Server package;
4. Logging package.
Первый пакет – Antivirus package. В данном пакете находятся модули, для обеспечения следующего функционала:
1. Идентификация и аутентификация. 
Данный модуль предоставляет функционал для входа в Систему. Модуль содержит:
  аутентификацию. Должностное лицо, должно войти в систему при по-мощи логина и пароля. 
  идентификацию. Систему сверяется с введёнными данными. Если вве-дённые данные верны, то пользователю должностное лицо подтвердить вход по e-mail адресу.
После успешной идентификации приходит письмо с кодом для входа в Систему. В дальнейшем планируется возможность получения кода по номеру телефона.
2. Сканер портов.
Данный модуль предоставляет функционал для поиска открытых портов IP-адреса, на котором располагается сервер. Сканирование портов может по-мочь определить потенциальные цели атаки, а также выяснить какие порты открыты, закрыты и используются операционной системой.
3. Отслеживание процессов.
Данный модуль позволяет отслеживать процессы, для выявления вирус-ной активности и следить за системными ресурсами.
4. Отслеживание файловых операций.
Данный модуль нужен для динамического анализа вредоносного кода.
5. Сбор информации о системе.
Данный модуль позволяет узнать более точную информацию об операционной системе на которой установлена Система.
6. Проверка файла.
В данный модуль можно загрузить файл и получить всю информацию о нём, а также узнать содержит ли этот файл вредоносный код.
Во время разработки возможно добавление нового функционала или от-каз от ненужного.
Второй пакет – Database package.
В данном пакете находится модуль системы управления базами данных (далее - СУБД). Данный модуль необходим для изменения, удаления, добавления данных в базах данных, а также для создания новых баз данных.
Третий пакет – Logging package.
Данный модуль создаёт журнал действий для регистрации всех действий пользователя.
Четвёртый пакет – Server package.
В данном модуле находится серверный файл при помощи которого осу-ществляется для удалённого подключение к нужной базе данных. При помощи этого модуля пользователь может взаимодействовать со своими данными.
Пятый пакет – Client package.
В данном модуле находится клиентский файл. Данный файл поставля-ется пользователю для удалённого просмотра, внесения изменений данных.
Шестой пакет – SSL package.
Данный пакет предоставляет ssl-сертификат для обеспечения  безопасно-го подключения пользователя к серверу.
Типы пользователей.
Системе предусматривает два типа пользователей: сотрудник и обычный пользователь.
Сотрудник – пользователь, который работает в отделе и занимается обеспечением защиты информации.
Обычный пользователь – пользователь, которому нужно посмотреть свои персональные данные.
Доступ в Систему.
При запуске Система предлагает войти должностному лицу с имеющимися данными или создать аккаунт для входа. Обычному пользователю предоставляется такой же функционал.
Регистрация в Системе предусматривает передачу следующих данных:
1. Email (email) – обязательное поле;
2. Login (логин) – обязательное поле;
3. Password (пароль) – обязательное поле.
В дальнейшем email будет использоваться для прохождения двухфакторной аутентификации. 
Аутентификация в Системе осуществляется при помощи логина и па-роля. Если переданные данные прошли проверку, необходимо ввести код, который придёт по почте. 
Предлагаемый стек технологий.
Для реализации Системы предлагается следующий стек технологий:
1. Язык программирования – Python;
2. Библиотеки:
  os - для взаимодействия с файловыми директориями операционной си-стемы;
  threading - обеспечивает работу модулей в многопоточном режиме;
  sqlite3 - встроенная СУБД;
  socket - для создания сервера на TCP/IP сетевой модели передачи дан-ных;
  smtplib - предоставляет функционал для отправки email сообщений;
  string - содержит в себе набор констант букв в верхнем и нижнем реги-стре, цифр и других символов;
  random - создаёт случайную последовательность из чисел;
  email - для оформления email сообщения;
  usb - обеспечивает взаимодействие с usb устройствами;
  datetime - предлагает широкий функционал для работы с датой и временем
  loguru - необходим для регистрации внутренних действий программы
  time - предлагает инструменты для создания таймера
  platform -включает в себя инструменты для получений сведений об ап-паратной платформе, операционной системе и интерпретаторе на которой вы-полняется программа;
  psutil - для работы с системными процессами;
  json - формат для обмена данными, позволяет кодировать и декодиро-вать данные удобном формате;
  ssl - обеспечивает шифрование и одноранговую аутентификацию для сетевых сокетов, как на стороне клиента, так и на стороне сервера.
  openSSl - предоставляет высокуровневый интерфейс для работы с ssl шифрование;
  hashlib - предоставляет интерфейс для реализации множества различ-ных безопасных алгоритмов хеширования и дайджеста сообщений;
  crypto - набор. как безопасных хэш-функций, так и различных алгоритмов шифрования; 
  PyQt5 - высокоуровневая библиотека для создания графического ин-терфейса.
В процессе разработки некоторые библиотеки могут удаляться, а также добавляться новые.
Блок-схема
На рисунке 1 представлена блок-схема, отражающая работу и взаимодействие модулей друг с другом в Системе.
 
Рисунок 1 – схема работы Системы
Требования к дизайну.
В данный момент программа работает в консольном окне операционной системы. В последующем будет разработан графический интерфейс для более удобной работы с Системой.