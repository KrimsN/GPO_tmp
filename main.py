"""
Copyright (c) 2018-2019, Pentagon Developments Cooperations
All rights reserved.

Redistribution and use in source and binary forms, with or without modification, are
permitted provided that the following conditions are met:

   1. Redistributions of source code must retain the above copyright notice, this list of
      conditions and the following disclaimer.

   2. Redistributions in binary form must reproduce the above copyright notice, this list
      of conditions and the following disclaimer in the documentation and/or other materials
      provided with the distribution.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY
EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF
MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE
COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL,
EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION)
HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR
TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS
SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
"""

import time
import argparse 


import gosat_module as gosat
import tansat_module as tansat
import oco2_module as oco2


def main():
    parser = argparse.ArgumentParser()
    #parser.add_argument('module', help='Спутник, с которым необходимо работать', choices=['GOSAT', 'OCO2', 'TANSAT'])
    parser.add_argument('--gosat', help='Получать данные со спутника GOSAT', action='store_true', default=False)
    parser.add_argument('--tansat', help='Получать данные со спутника TANSAT', action='store_true', default=False)
    parser.add_argument('--oco2', help='Получать данные со спутника OCO2', action='store_true', default=False)
    parser.add_argument('--update_time', help='Таймер проверки новых данных (в днях)', type=float, action='store', default=0)
    parser.add_argument('--debug', help='Enable debug mod', action='store_true', default=False)
    args = parser.parse_args()

    try:
        # get time from days to seconds
        update_time = int(args.update_time * 24 * 60 * 60)
            
        while True:
            if args.gosat:
                pass


            if args.tansat:
                pass


            if args.oco2:
                pass
            
            if args.update_time < 1:
                break
            else:
                time.sleep(update_time)

    except:
        pass

    finally:
        pass

    




if __name__ == "__main__":
    main()