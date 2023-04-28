from multiprocessing import freeze_support

import audalign as ad

if __name__ == '__main__':
    freeze_support()

    fingerprint_rec = ad.FingerprintRecognizer()
    # correlation_rec = ad.CorrelationRecognizer()
    # cor_spec_rec = ad.CorrelationSpectrogramRecognizer()
    # visual_rec = ad.VisualRecognizer(

    # inputsのフォルダにある音声ファイルをoutputフォルダに位置合わせして出力
    result = ad.align(
        "inputs",
        destination_path="output",
        recognizer=fingerprint_rec,
    )

    # print(result)