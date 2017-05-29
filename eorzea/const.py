class SexMapping:
    SEX_UNKNOW = 1
    SEX_MAN = 2
    SEX_WOMAN = 3


def get_sex(key):
    mapping = {
        SexMapping.SEX_UNKNOW: "unknow",
        SexMapping.SEX_MAN: "man",
        SexMapping.SEX_WOMAN: "woman"
    }

    return mapping.get(key)
