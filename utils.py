from pypinyin import pinyin
import shutil
import os


def move_file(folders, datasets, uids, result):
    for folder in folders:
        if folder.split("/")[-1].split("_")[-1] == "gt":
            setting = "gt"
        elif "no_casting" in folder:
            setting = "mscqtd_none"
        elif "mscqtd" in folder:
            setting = "mscqtd"
        else:
            setting = "orig"
        for i, (dataset, uid) in enumerate(zip(datasets, uids)):
            if setting == "gt" or setting == "gt_speech":
                old_file = folder + "/{}".format(dataset) + "/{}.wav".format(uid)
            else:
                old_file = folder + "/{}".format(dataset) + "/{}_pred.wav".format(uid)
            if "speech" in setting:
                setting = setting.split("_")[0]
            new_file = result + "/{}_{}.wav".format(i + 1, setting)
            print(old_file)
            print(new_file)
            shutil.copyfile(old_file, new_file)


def get_pinyin(lyric):
    results = pinyin(lyric)
    ans = []
    for result in results:
        ans.append(result[0])
    return " ".join(ans)


if __name__ == "__main__":
    ### Seen
    # datasets = [
    #     "opencpopbeta",
    #     "opencpopbeta",
    #     "m4singer",
    #     "m4singer",
    #     "m4singer",
    # ]
    # uids = [
    #     "1044003410",
    #     "1092002291",
    #     "Alto-1_美错_0014",
    #     "Bass-1_十年_0008",
    #     "Soprano-2_同桌的你_0018",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_orig",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_msstftd",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_mscqtd",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_merge",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/effectiveness"
    ### Unseen
    # datasets = [
    #     "popcs",
    #     "popcs",
    #     "opensinger",
    #     "opensinger",
    #     "opensinger",
    # ]
    # uids = [
    #     "明天会更好_0016",
    #     "隐形的翅膀_0009",
    #     "Man_21_丑八怪_8",
    #     "Man_0_大鱼_19",
    #     "Woman_40_易燃易爆炸_12",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_orig",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_msstftd",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_mscqtd",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_merge",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/effectiveness"
    # move_file(folders, datasets, uids, result)
    ### Seen
    # datasets = [
    #     "ljspeech",
    #     "libritts",
    #     "libritts",
    #     "libritts",
    #     "ljspeech",
    # ]
    # uids = [
    #     "LJ001-0051",
    #     "233_155990_233_155990_000006_000007",
    #     "233_155990_233_155990_000007_000006",
    #     "696_92939_696_92939_000002_000000",
    #     "LJ006-0009",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt_speech",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_orig_speech",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_msstftd_speech",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_mscqtd_speech",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/hifigan_merge_speech",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/effectiveness"
    # move_file(folders, datasets, uids, result)
    ### Unseen
    # datasets = [
    #     "opensinger",
    #     "opensinger",
    #     "opensinger",
    # ]
    # uids = [
    #     "Man_0_大鱼_15",
    #     "Woman_39_mojito_10",
    #     "Woman_40_易燃易爆炸_25",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/melgan_orig",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/melgan_merge",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/generalization/melgan"
    # move_file(folders, datasets, uids, result)
    ### Seen
    # datasets = [
    #     "m4singer",
    #     "opencpopbeta",
    #     "m4singer",
    # ]
    # uids = [
    #     "Alto-1_美错_0010",
    #     "1092002304",
    #     "Bass-1_十年_0001",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/nsfhifigan_orig",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/nsfhifigan_merge",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/generalization/nsfhifigan"
    # move_file(folders, datasets, uids, result)
    ### Unseen
    # datasets = [
    #     "popcs",
    #     "opensinger",
    #     "popcs",
    # ]
    # uids = [
    #     "隐形的翅膀_0004",
    #     "Man_0_大鱼_12",
    #     "虫儿飞_0001",
    # ]
    # folders = [
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/nsfhifigan_orig",
    #     "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/nsfhifigan_merge",
    # ]
    # result = "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/generalization/nsfhifigan"
    ### Ablation
    datasets = [
        "opencpop",
        "opencpop",
        "opencpop",
    ]
    uids = [
        "2044001646",
        "2086003180",
        "2093003455",
    ]
    folders = [
        "D:/Study/CUHKSZ/Research_Group/ICASSP2024/tmp/gt",
        "D:/Study/CUHKSZ/Research_Group/ICASSP2024/ablasion_hifigan",
        "D:/Study/CUHKSZ/Research_Group/ICASSP2024/ablasion_hifigan_mscqtd",
        "D:/Study/CUHKSZ/Research_Group/ICASSP2024/ablasion_hifigan_mscqtd_no_casting",
    ]
    result = (
        "D:/Study/CUHKSZ/Research_Group/ICASSP2024/MS-SB-CQTD/assets/audios/ablation"
    )
    move_file(folders, datasets, uids, result)
    # print(get_pinyin("为我撩人,还为我双眸失神"))
