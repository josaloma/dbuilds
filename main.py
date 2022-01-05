
import time

class Testi:
    def __init__(self):
        self.teksti = "Docker works! Local time:"
        #print("käynnistää")
        self.kaynnista() # käynnistetään peli



    def kaynnista(self):
        sekunnit = time.time()
        paikallinen = time.ctime(sekunnit)
        #print("Local time:", paikallinen)	
        while True:
            kulunut = time.time()-sekunnit
            #print(kulunut)
            if kulunut > 5:
                sekunnit = time.time()
                paikallinen = time.ctime(sekunnit)
                print(self.teksti + paikallinen)



if __name__ == "__main__":

    Testi()
