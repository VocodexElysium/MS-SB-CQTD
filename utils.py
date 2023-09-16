from pypinyin import pinyin
import shutil
import os


def move_file(folders, datasets, uids, result):
    for folder in folders:
        setting = folder.split("/")[-1].split("_")[-1]
        for i, (dataset, uid) in enumerate(zip(datasets, uids)):
            if setting == "gt":
                old_file = folder + "/{}".format(dataset) + "/{}.wav".format(uid)
            else:
                old_file = folder + "/{}".format(dataset) + "/{}_pred.wav".format(uid)
            new_file = result + "/seen_singer_{}_{}.wav".format(i + 1, setting)
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
    print(get_pinyin("美丽的错误往往最接近真实"))
