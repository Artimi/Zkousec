#!/usr/bin/env python
#-*- coding: UTF-8 -*-

import random
import sys
import time
import datetime
from questions import questions

preparation_time = 4

def test(question_number):
    q = questions[question_number]
    q_list = q[1][:]
    print "--------------------------------------------------------------------------------"
    print q[0]
    prep = raw_input("Chceš využít čas na přípravu? (Implicitně ano, pro ne napiš \"n\")")
    if prep != "n":
        timeout = preparation_time
        start_time = time.time()
        while timeout > 0:
            sys.stdout.write("\r{0} s do začátku".format(datetime.timedelta(seconds=timeout)))
            sys.stdout.flush()
            timeout = preparation_time - int(time.time()-start_time)
            time.sleep(1)
    sys.stdout.write("\rStisknutím Enteru bude položena otázka. Pro skončení napište \"exit\"")
    start_time = time.time()
    while True:
        s = raw_input()
        if s == "exit":
            break
        try:
            current_q = random.choice(q_list)
            q_list.remove(current_q)
            print current_q
        except IndexError:
            print "Nejsou dostupné další otázky"
        print "Čas:", datetime.timedelta(seconds=int(time.time()-start_time))
    print


if __name__ == '__main__':
    try:
        while 1:
            test(random.randint(0, 39))
    except KeyboardInterrupt:
        pass
