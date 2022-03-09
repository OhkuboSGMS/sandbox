# cv2_resize
opencvのimage(numpy.ndarray)をリサイズする機能

### cv2.resizeとの違い
* width,heightどちらか一方を与えると、アスペクト比を考慮してリサイズできる
* width,height両方を与えると、指定された画像サイズに収まるようにリサイズする、その際余った部分は背景として色を指定できる
* 一つの関数で引数の与え方を変えることで上記のリサイズを実現


## Install from git
`pip install git+https://github.com/OhkuboSGMS/sandbox.git#egg=cv_resize&subdirectory=resize `

## Demo

TODO implements
