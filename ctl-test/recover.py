import os

filepath='./'
def split(string,symbol):
        pos=string.find(symbol)
        return string[2:pos]

def askq(string):
        ans=input(string+'\n-->')
        if ans=='y':
                return 1
        elif ans=='n':
                return 0
        elif ans=='q':
                return 2
        else:
                print('ans error')
                askq(string)


def main():
        f=open(filepath+'errremove.txt','r')
        log=open(filepath+'rec-log.txt','w+')
        str=f.readline()
        num=1
        while(str!=''):
                codetail=split(str,':')
                ask=askq('Do you want to install '+codetail)
                if ask==1:
                        log.write('y '+codetail)
                        os.system('sudo apt-fast install '+codetail)
                elif ask==2:
                        os.system('firefox www.baidu.com\#wd='+codetail)
                        ask2=askq('y or n?')
                        if ask2==1:
                                log.write('y '+codetail)
                                os.system('sudo apt-fast install '+codetail)
                elif ask==0:
                        log.write('n '+codetail)
                rest=input('anything else log?\n-->')
                if rest=='?':
                        log.write('? '+codetail+'\n')
                else:
                        print('error input')
                        continue
                print(num)
                print('\n')
                num+=1
                str=f.readline()
main()

