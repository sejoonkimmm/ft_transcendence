AVATAR_CHOICES = [
    (0, "chewbacca.png"),
    (1, "darth_vader.png"),
    (2, "luke_skywalker.png"),
    (3, "han_solo.png"),
    (4, "yoda.png"),
]

AVATAR_CHOICES_DICT = {
    0: "chewbacca.png",
    1: "darth_vader.png",
    2: "luke_skywalker.png",
    3: "han_solo.png",
    4: "yoda.png",
}

MODE_CHOICES = [
    (0, "casual_1vs1"),
    (1, "casual_tournament"),
    (2, "rank"),
]

MODE_CHOICES_DICT = dict(MODE_CHOICES)

MODE_CHOICES_REVERSE_DICT = {
    v: k for k, v in MODE_CHOICES_DICT.items()
}

STATUS_CHOICES = [
    (0, "AVAILABLE_WAITING"),
    (1, "FULL_WAITING"),
    (2, "IN_GAME"),
    (3, "FINISHED"),
    (4, "DELETED"),
]

FRIENDS_CHOICES = [
    (0, "대기"),
    (1, "수락"),
    (2, "거절"),
]

GAME_SETTINGS_DICT = {
    'bar': {
        'width': 10,
        'height': 100,
        'speed': 10
    },
    'ball': {
        'radius': 10,
        'speed': 10
    }
}
