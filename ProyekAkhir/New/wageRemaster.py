import mainFunction as mf
import necessaryFunction as nf
import object as obj

def main():
    mf.dir_setup()
    obj.logo()
    nf.delay(1.5)
    mf.run()

if __name__ == '__main__':
    main()