import subprocess
import client_io
import os.path

IP = '192.168.11.xxx'
PORT = 22222

def make_wav(text, output_path=os.getcwd()):
    """
    引数textで与えた文字列を音声合成し、現在のディレクトリに
    __temp.wavという名前で出力する関数
    """
    OPENJTALK_BINPATH = '/usr/bin'
    OPENJTALK_DICPATH = '/var/lib/mecab/dic/open-jtalk/naist-jdic'
    OPENJTALK_VOICEPATH = '/usr/share/hts-voice/mei/mei_normal.htsvoice'
    open_jtalk = [OPENJTALK_BINPATH + '/open_jtalk']
    mech = ['-x',OPENJTALK_DICPATH]
    htsvoice = ['-m',OPENJTALK_VOICEPATH]
    speed = ['-r','1.0']
    outwav = ['-ow', os.path.join(output_path, '__temp.wav')]
    cmd = open_jtalk + mech + htsvoice + speed + outwav
    c = subprocess.Popen(cmd,stdin=subprocess.PIPE)
    c.stdin.write(text.encode('utf-8'))
    c.stdin.close()
    c.wait()

def send_wav():
    """
    __temp.wavをSotaに送信する関数
    """
    with open('__temp.wav', 'rb') as f:
        data = f.read()
        cli = client_io.MyClient()
        cli.connect(IP, PORT)
        cli.write(data)
        cli.close()

if __name__ == '__main__':
    make_wav("こんにちは")
    send_wav()