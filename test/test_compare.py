# -*- coding: utf-8 -*-
from .helper import check_evaluation
import pytest

#  The following tests where generated automatically calling wolframscript -c
#  followed by a combination of expressions.
#  This is the code I used to generate them
#
#  %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
#  import subprocess
#  from time import sleep
#  exprss = ['2 + 3*a', 'Infinity', '-Infinity', 'Sqrt[I] Infinity', 'a', '"a"', '"1/4"', "I", "0", '1/4','.25',"Sqrt[2]", "BesselJ[0,2]", "3+2 I", "2.+ Pi I", "3+Pi I", 'StringStream["Tengo una vaca lechera"]', "Compile[{x},Sqrt[x]]", "Graphics[{Disk[{0,0},1]}]"]
#  exprs = [ lhs + '=='+ rhs for lhs in exprss for rhs in exprss]
#  tests = []
#  for expr in exprs:
#      result = subprocess.run(['wolframscript', '-c', expr], stdout=subprocess.PIPE)
#      sleep(1)
#      res = result.stdout.decode('utf8').strip()
#      if len(res)>0 and res[-1]=='\n':
#          res = res[:-2]
#      tests.append((expr, res))
#  tests
#


# In Mathics, DirectedInfinity[(-1)^(1/4)] (WMA) ->  System`Times[System`Power[I, 1/2], System`DirectedInfinity[1]]]


#@pytest.mark.skip(reason="fixes in progress...")
@pytest.mark.parametrize(
    ("str_expr", "str_expected"),
    [
                ("Infinity==3+2 I", "False"),
                (
                    '2 + 3*a==StringStream["Tengo una vaca lechera"]',
                    '2 + 3*a == StringStream["Tengo una vaca lechera"]',
                ),
                 ("-Infinity==I", "False"),
        (
            "Infinity==Compile[{x},Sqrt[x]]",
            "Infinity==Compile[{x},Sqrt[x]]",
         ),
         ("Sqrt[I] Infinity==I", "False"),
         ("Sqrt[I] Infinity==0", "False"),
         ("Sqrt[I] Infinity==1/4", "False"),
         ("Sqrt[I] Infinity==3+2 I", "False"),
         ('"a"==.25', "False"),
         ('"a"==2.+ Pi I', "False"),
         ('"1/4"==.25', "False"),
         ('"1/4"==2.+ Pi I', "False"),
         ("I==Infinity", "False"),
         ("I==-Infinity", "False"),
         ("I==Sqrt[I] Infinity", "False"),
         ("I==.25", "False"),
         ("I==Sqrt[2]", "False"),
         ("I==BesselJ[0,2]", "False"),
         ("I==2.+ Pi I", "False"),
          ("-Infinity==3+2 I", "False"),
         ("Sqrt[I] Infinity==Infinity", "False"),
                            ("I==3+Pi I", "False"),
                     (
              "I==Compile[{x},Sqrt[x]]",
             "I == Compile[{x},Sqrt[x]]",
             ),
         (
            '0==StringStream["Tengo una vaca lechera"]',
            "0 == StringStream[\"Tengo una vaca lechera\"]",
         ),
         ("0==Infinity", "False"),
         ("0==-Infinity", "False"),
         ("0==Sqrt[I] Infinity", "False"),
         ("0==2.+ Pi I", "False"),
         ("0==3+Pi I", "False"),
         ("0==3+2 I", "False"),
         ("1/4==Sqrt[I] Infinity", "False"),
         ("1/4==2.+ Pi I", "False"),
         ("1/4==3+Pi I", "False"),
         (
            '1/4==StringStream["Tengo una vaca lechera"]',
            "1/4 == StringStream[\"Tengo una vaca lechera\"]",
         ),
                 ("2 + 3*a==Sqrt[I] Infinity", "2 + 3*a == DirectedInfinity[(-1)^(1/4)]"),
        (
            'Infinity==StringStream["Tengo una vaca lechera"]',
            'Infinity == StringStream["Tengo una vaca lechera"]',
        ),
        ("Infinity==Graphics[{Disk[{0,0},1]}]", "Infinity==Graphics[{Disk[{0,0},1]}]",),
        ("2 + 3*a==2.+ Pi I", "2 + 3*a == 2. + 3.141592653589793*I"),
        ("2 + 3*a==BesselJ[0,2]", "2 + 3*a == BesselJ[0, 2]"),
        ("2 + 3*a==3+2 I", "2 + 3*a == 3 + 2*I"),
        (
            "2 + 3*a==Compile[{x},Sqrt[x]]",
            "2 + 3*a==Compile[{x},Sqrt[x]]",
        ),
        (
            "2 + 3*a==Graphics[{Disk[{0,0},1]}]",
            "2 + 3*a == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        ("Infinity==2 + 3*a", "Infinity == 2 + 3*a"),
        ("Infinity==Infinity", "True"),
        ("Infinity==-Infinity", "False"),
        # For WMA, the next one evaluated to False
        ("Infinity==Sqrt[I] Infinity", "Infinity==Sqrt[I] Infinity"),
        ("Infinity==a", "Infinity == a"),
        ('Infinity=="a"', 'Infinity == "a"'),
        ('Infinity=="1/4"', 'Infinity == "1/4"'),
        ("Infinity==0", "False"),
        ("Infinity==1/4", "False"),
        ("Infinity==.25", "False"),
        ("Infinity==Sqrt[2]", "False"),
        ("Infinity==BesselJ[0,2]", "False"),
        ("Infinity==2.+ Pi I", "False"),
        ("Infinity==3+Pi I", "False"),
        ("-Infinity==Infinity", "-Infinity==Infinity"),
        ("-Infinity==-Infinity", "True"),
        ("-Infinity==Sqrt[I] Infinity", "-Infinity==Sqrt[I] Infinity"),
        ("-Infinity==a", "-Infinity==a"),
        ('-Infinity=="a"', '-Infinity=="a"'),
        ('-Infinity=="1/4"', '-Infinity=="1/4"'),
        ("-Infinity==0", "False"),
        ("-Infinity==1/4", "False"),
        ("-Infinity==.25", "False"),
        ("-Infinity==Sqrt[2]", "False"),
        ("-Infinity==BesselJ[0,2]", "False"),
        ("-Infinity==2.+ Pi I", "False"),
        ("-Infinity==3+Pi I", "False"),
        (
            '-Infinity==StringStream["Tengo una vaca lechera"]',
            '-Infinity==StringStream["Tengo una vaca lechera"]',
        ),
        ("-Infinity==Compile[{x},Sqrt[x]]", "False"),
        (
            "-Infinity==Graphics[{Disk[{0,0},1]}]",
            "-Infinity==Graphics[{Disk[{0,0},1]}]",
        ),
        (
            "Sqrt[I] Infinity==2 + 3*a",
            "Times[Power[I,1/2],DirectedInfinity[1]] == 2 + 3*a",
        ),
        ("Sqrt[I] Infinity==-Infinity", "False"),
        ("Sqrt[I] Infinity==Sqrt[I] Infinity", "True"),
        ("Sqrt[I] Infinity==a", "Times[Power[I,1/2],DirectedInfinity[1]] == a"),
        ('Sqrt[I] Infinity=="a"', 'Times[Power[I,1/2],DirectedInfinity[1]] == "a"'),
        ('Sqrt[I] Infinity=="1/4"', 'Times[Power[I,1/2],DirectedInfinity[1]] == "1/4"'),
        ("Sqrt[I] Infinity==.25", "False"),
        ("Sqrt[I] Infinity==Sqrt[2]", "False"),
        ("Sqrt[I] Infinity==BesselJ[0,2]", "False"),
        ("Sqrt[I] Infinity==2.+ Pi I", "False"),
        ("Sqrt[I] Infinity==3+Pi I", "False"),
        (
            'Sqrt[I] Infinity==StringStream["Tengo una vaca lechera"]',
            'Times[Power[I,1/2],DirectedInfinity[1]] == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "Sqrt[I] Infinity==Compile[{x},Sqrt[x]]",
            "Sqrt[I] Infinity==Compile[{x},Sqrt[x]]",
        ),
        (
            "Sqrt[I] Infinity==Graphics[{Disk[{0,0},1]}]",
            "Times[Power[I,1/2],DirectedInfinity[1]] == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        ("a==2 + 3*a", "a == 2 + 3*a"),
        ("a==Infinity", "a == Infinity"),
        ("a==-Infinity", "a == -Infinity"),
        ("a==Sqrt[I] Infinity", "a == Times[Power[I,1/2],DirectedInfinity[1]]"),
        ("a==a", "True"),
        ('a=="a"', 'a == "a"'),
        ('a=="1/4"', 'a == "1/4"'),
        ("a==I", "a == I"),
        ("a==0", "a == 0"),
        ("a==1/4", "a == 1/4"),
        ("a==.25", "a == 0.25"),
        ("a==Sqrt[2]", "a == Sqrt[2]"),
        ("a==BesselJ[0,2]", "a == BesselJ[0, 2]"),
        ("a==3+2 I", "a == 3 + 2*I"),
        ("a==2.+ Pi I", "a == 2. + 3.141592653589793*I"),
        ("a==3+Pi I", "a == 3 + I*Pi"),
        (
            'a==StringStream["Tengo una vaca lechera"]',
            'a == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "a==Compile[{x},Sqrt[x]]",
            "a==Compile[{x},Sqrt[x]]",
        ),
        ("a==Graphics[{Disk[{0,0},1]}]", "a == Graphics[{Disk[{0, 0}, 1]}]"),
        ('"a"==2 + 3*a', '"a" == 2 + 3*a'),
        ('"a"==Infinity', '"a" == Infinity'),
        ('"a"==-Infinity', '"a" == -Infinity'),
        ('"a"==Sqrt[I] Infinity', '"a" == Times[Power[I,1/2],DirectedInfinity[1]]'),
        ('"a"==a', '"a" == a'),
        ('"a"=="a"', "True"),
        ('"a"=="1/4"', "False"),
        ('"a"==I', "False"),
        ('"a"==0', "False"),
        ('"a"==1/4', "False"),
        ('"a"==Sqrt[2]', '"a" == Sqrt[2]'),
        ('"a"==BesselJ[0,2]', '"a" == BesselJ[0, 2]'),
        ('"a"==3+2 I', "False"),
        ('"a"==3+Pi I', '"a" == 3 + I*Pi'),
        (
            '"a"==StringStream["Tengo una vaca lechera"]',
            '"a" == StringStream["Tengo una vaca lechera"]',
        ),
        (
            '"a"==Compile[{x},Sqrt[x]]',
            '"a"==Compile[{x},Sqrt[x]]',
        ),
        ('"a"==Graphics[{Disk[{0,0},1]}]', '"a" == Graphics[{Disk[{0, 0}, 1]}]'),
        ('"1/4"==2 + 3*a', '"1/4" == 2 + 3*a'),
        ('"1/4"==Infinity', '"1/4" == Infinity'),
        ('"1/4"==-Infinity', '"1/4" == -Infinity'),
        ('"1/4"==Sqrt[I] Infinity', '"1/4" == Times[Power[I,1/2],DirectedInfinity[1]]'),
        ('"1/4"==a', '"1/4" == a'),
        ('"1/4"=="a"', "False"),
        ('"1/4"=="1/4"', "True"),
        ('"1/4"==I', "False"),
        ('"1/4"==0', "False"),
        ('"1/4"==1/4', "False"),
        ('"1/4"==Sqrt[2]', '"1/4" == Sqrt[2]'),
        ('"1/4"==BesselJ[0,2]', '"1/4" == BesselJ[0, 2]'),
        ('"1/4"==3+2 I', "False"),
        ('"1/4"==3+Pi I', '"1/4" == 3 + I*Pi'),
        (
            '"1/4"==StringStream["Tengo una vaca lechera"]',
            '"1/4" == StringStream["Tengo una vaca lechera"]',
        ),
        (
            '"1/4"==Compile[{x},Sqrt[x]]',
            '"1/4"==Compile[{x},Sqrt[x]]',
        ),
        ('"1/4"==Graphics[{Disk[{0,0},1]}]', '"1/4" == Graphics[{Disk[{0, 0}, 1]}]'),
        ("I==2 + 3*a", "I == 2 + 3*a"),
        ("I==a", "I == a"),
        ('I=="a"', "False"),
        ('I=="1/4"', "False"),
        ("I==I", "True"),
        ("I==0", "False"),
        ("I==1/4", "False"),
        ("I==3+2 I", "False"),
        (
            'I==StringStream["Tengo una vaca lechera"]',
            'I == StringStream["Tengo una vaca lechera"]',
        ),
        ("I==Graphics[{Disk[{0,0},1]}]", "I == Graphics[{Disk[{0, 0}, 1]}]"),
        ("0==2 + 3*a", "0 == 2 + 3*a"),
        ("0==a", "0 == a"),
        ('0=="a"', "False"),
        ('0=="1/4"', "False"),
        ("0==I", "False"),
        ("0==0", "True"),
        ("0==1/4", "False"),
        ("0==.25", "False"),
        ("0==Sqrt[2]", "False"),
        ("0==BesselJ[0,2]", "False"),
        (
            "0==Compile[{x},Sqrt[x]]",
            "0==Compile[{x},Sqrt[x]]",
        ),
        ("0==Graphics[{Disk[{0,0},1]}]", "0 == Graphics[{Disk[{0, 0}, 1]}]"),
        ("1/4==2 + 3*a", "1/4 == 2 + 3*a"),
        ("1/4==Infinity", "False"),
        ("1/4==-Infinity", "False"),
        ("1/4==a", "1/4 == a"),
        ('1/4=="a"', "False"),
        ('1/4=="1/4"', "False"),
        ("1/4==I", "False"),
        ("1/4==0", "False"),
        ("1/4==1/4", "True"),
        ("1/4==.25", "True"),
        ("1/4==Sqrt[2]", "False"),
        ("1/4==BesselJ[0,2]", "False"),
        ("1/4==3+2 I", "False"),
        (
            "1/4==Compile[{x},Sqrt[x]]",
            "1/4==Compile[{x},Sqrt[x]]",
        ),
        ("1/4==Graphics[{Disk[{0,0},1]}]", "1/4 == Graphics[{Disk[{0, 0}, 1]}]"),
        (".25==2 + 3*a", "0.25 == 2 + 3*a"),
        (".25==Infinity", "False"),
        (".25==-Infinity", "False"),
        (".25==Sqrt[I] Infinity", "False"),
        (".25==a", "0.25 == a"),
        ('.25=="a"', "False"),
        ('.25=="1/4"', "False"),
        (".25==I", "False"),
        (".25==0", "False"),
        (".25==1/4", "True"),
        (".25==.25", "True"),
        (".25==Sqrt[2]", "False"),
        (".25==BesselJ[0,2]", "False"),
        (".25==3+2 I", "False"),
        (".25==2.+ Pi I", "False"),
        (".25==3+Pi I", "False"),
        (
            '.25==StringStream["Tengo una vaca lechera"]',
            '0.25 == StringStream["Tengo una vaca lechera"]',
        ),
        (
            ".25==Compile[{x},Sqrt[x]]",
            ".25==Compile[{x},Sqrt[x]]",
        ),
        (".25==Graphics[{Disk[{0,0},1]}]", "0.25 == Graphics[{Disk[{0, 0}, 1]}]"),
        ("Sqrt[2]==2 + 3*a", "Sqrt[2] == 2 + 3*a"),
        ("Sqrt[2]==Infinity", "False"),
        ("Sqrt[2]==-Infinity", "False"),
        ("Sqrt[2]==Sqrt[I] Infinity", "False"),
        ("Sqrt[2]==a", "Sqrt[2] == a"),
        ('Sqrt[2]=="a"', "Sqrt[2] == \"a\""),
        ('Sqrt[2]=="1/4"', "Sqrt[2] == \"1/4\""),
        ("Sqrt[2]==I", "False"),
        ("Sqrt[2]==0", "False"),
        ("Sqrt[2]==1/4", "False"),
        ("Sqrt[2]==.25", "False"),
        ("Sqrt[2]==Sqrt[2]", "True"),
        ("Sqrt[2]==BesselJ[0,2]", "False"),
        ("Sqrt[2]==3+2 I", "False"),
        ("Sqrt[2]==2.+ Pi I", "False"),
        ("Sqrt[2]==3+Pi I", "False"),
        (
            'Sqrt[2]==StringStream["Tengo una vaca lechera"]',
            'Sqrt[2] == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "Sqrt[2]==Compile[{x},Sqrt[x]]",
            "Sqrt[2]==Compile[{x},Sqrt[x]]",
        ),
        (
            "Sqrt[2]==Graphics[{Disk[{0,0},1]}]",
            "Sqrt[2] == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        ("BesselJ[0,2]==2 + 3*a", "BesselJ[0, 2] == 2 + 3*a"),
        ("BesselJ[0,2]==Infinity", "False"),
        ("BesselJ[0,2]==-Infinity", "False"),
        ("BesselJ[0,2]==Sqrt[I] Infinity", "False"),
        ("BesselJ[0,2]==a", "BesselJ[0, 2] == a"),
        ('BesselJ[0,2]=="a"', "BesselJ[0, 2] == \"a\""),
        ('BesselJ[0,2]=="1/4"', "BesselJ[0, 2] == \"1/4\""),
        ("BesselJ[0,2]==I", "False"),
        ("BesselJ[0,2]==0", "False"),
        ("BesselJ[0,2]==1/4", "False"),
        ("BesselJ[0,2]==.25", "False"),
        ("BesselJ[0,2]==Sqrt[2]", "False"),
        ("BesselJ[0,2]==BesselJ[0,2]", "True"),
        ("BesselJ[0,2]==3+2 I", "False"),
        ("BesselJ[0,2]==2.+ Pi I", "False"),
        ("BesselJ[0,2]==3+Pi I", "False"),
        (
            'BesselJ[0,2]==StringStream["Tengo una vaca lechera"]',
            'BesselJ[0, 2] == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "BesselJ[0,2]==Compile[{x},Sqrt[x]]",
            "BesselJ[0,2]==Compile[{x},Sqrt[x]]",
        ),
        (
            "BesselJ[0,2]==Graphics[{Disk[{0,0},1]}]",
            "BesselJ[0, 2] == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        ("3+2 I==2 + 3*a", "3 + 2*I == 2 + 3*a"),
        ("3+2 I==Infinity", "False"),
        ("3+2 I==-Infinity", "False"),
        ("3+2 I==Sqrt[I] Infinity", "False"),
        ("3+2 I==a", "3 + 2*I == a"),
        ('3+2 I=="a"', "False"),
        ('3+2 I=="1/4"', "False"),
        ("3+2 I==I", "False"),
        ("3+2 I==0", "False"),
        ("3+2 I==1/4", "False"),
        ("3+2 I==.25", "False"),
        ("3+2 I==Sqrt[2]", "False"),
        ("3+2 I==BesselJ[0,2]", "False"),
        ("3+2 I==3+2 I", "True"),
        ("3+2 I==2.+ Pi I", "False"),
        ("3+2 I==3+Pi I", "False"),
        (
            '3+2 I==StringStream["Tengo una vaca lechera"]',
            '3 + 2*I == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "3+2 I==Compile[{x},Sqrt[x]]",
            "3+2 I==Compile[{x},Sqrt[x]]",
        ),
        ("3+2 I==Graphics[{Disk[{0,0},1]}]", "3 + 2*I == Graphics[{Disk[{0, 0}, 1]}]"),
        ("2.+ Pi I==2 + 3*a", "2. + 3.141592653589793*I == 2 + 3*a"),
        ("2.+ Pi I==Infinity", "False"),
        ("2.+ Pi I==-Infinity", "False"),
        ("2.+ Pi I==Sqrt[I] Infinity", "False"),
        ("2.+ Pi I==a", "2. + 3.141592653589793*I == a"),
        ('2.+ Pi I=="a"', "False"),
        ('2.+ Pi I=="1/4"', "False"),
        ("2.+ Pi I==I", "False"),
        ("2.+ Pi I==0", "False"),
        ("2.+ Pi I==1/4", "False"),
        ("2.+ Pi I==.25", "False"),
        ("2.+ Pi I==Sqrt[2]", "False"),
        ("2.+ Pi I==BesselJ[0,2]", "False"),
        ("2.+ Pi I==3+2 I", "False"),
        ("2.+ Pi I==2.+ Pi I", "True"),
        ("2.+ Pi I==3+Pi I", "False"),
        (
            '2.+ Pi I==StringStream["Tengo una vaca lechera"]',
            '2. + 3.141592653589793*I == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "2.+ Pi I==Compile[{x},Sqrt[x]]",
            "2. + 3.141592653589793*I == Compile[{x},Sqrt[x]]",
        ),
        (
            "2.+ Pi I==Graphics[{Disk[{0,0},1]}]",
            "2. + 3.141592653589793*I == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        ("3+Pi I==2 + 3*a", "3 + I*Pi == 2 + 3*a"),
        ("3+Pi I==Infinity", "False"),
        ("3+Pi I==-Infinity", "False"),
        ("3+Pi I==Sqrt[I] Infinity", "False"),
        ("3+Pi I==a", "3 + I*Pi == a"),
        ('3+Pi I=="a"', "3 + I*Pi == \"a\""),
        ('3+Pi I=="1/4"', "3 + I*Pi == \"1/4\""),
        ("3+Pi I==I", "False"),
        ("3+Pi I==0", "False"),
        ("3+Pi I==1/4", "False"),
        ("3+Pi I==.25", "False"),
        ("3+Pi I==Sqrt[2]", "False"),
        ("3+Pi I==BesselJ[0,2]", "False"),
        ("3+Pi I==3+2 I", "False"),
        ("3+Pi I==2.+ Pi I", "False"),
        ("3+Pi I==3+Pi I", "True"),
        (
            '3+Pi I==StringStream["Tengo una vaca lechera"]',
            '3 + I*Pi == StringStream["Tengo una vaca lechera"]',
        ),
        (
            "3+Pi I==Compile[{x},Sqrt[x]]",
            "3 + I*Pi == Compile[{x},Sqrt[x]]",
        ),
        (
            "3+Pi I==Graphics[{Disk[{0,0},1]}]",
            "3 + I*Pi == Graphics[{Disk[{0, 0}, 1]}]",
        ),
        (
            'StringStream["Tengo una vaca lechera"]==2 + 3*a',
            'StringStream["Tengo una vaca lechera"] == 2 + 3*a',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==Infinity',
            'StringStream["Tengo una vaca lechera"] == Infinity',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==-Infinity',
            'StringStream["Tengo una vaca lechera"] == -Infinity',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==Sqrt[I] Infinity',
            'StringStream["Tengo una vaca lechera"] == Times[Power[I,1/2],DirectedInfinity[1]]',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==a',
            'StringStream["Tengo una vaca lechera"] == a',
        ),
        (
            'StringStream["Tengo una vaca lechera"]=="a"',
            'StringStream["Tengo una vaca lechera"] == \"a\"',
        ),
        (
            'StringStream["Tengo una vaca lechera"]=="1/4"',
            'StringStream["Tengo una vaca lechera"] == \"1/4\"',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==I',
            'StringStream["Tengo una vaca lechera"] == I',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==0',
            'StringStream["Tengo una vaca lechera"] == 0',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==1/4',
            'StringStream["Tengo una vaca lechera"] == 1/4',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==.25',
            'StringStream["Tengo una vaca lechera"] == 0.25',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==Sqrt[2]',
            'StringStream["Tengo una vaca lechera"] == Sqrt[2]',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==BesselJ[0,2]',
            'StringStream["Tengo una vaca lechera"] == BesselJ[0, 2]',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==3+2 I',
            'StringStream["Tengo una vaca lechera"] == 3 + 2*I',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==2.+ Pi I',
            'StringStream["Tengo una vaca lechera"] == 2. + 3.141592653589793*I',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==3+Pi I',
            'StringStream["Tengo una vaca lechera"] == 3 + I*Pi',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==StringStream["Tengo una vaca lechera"]',
            "True",
        ),
        (
            'StringStream["Tengo una vaca lechera"]==Compile[{x},Sqrt[x]]',
            'StringStream["Tengo una vaca lechera"] == Compile[{x},Sqrt[x]]',
        ),
        (
            'StringStream["Tengo una vaca lechera"]==Graphics[{Disk[{0,0},1]}]',
            'StringStream["Tengo una vaca lechera"] == Graphics[{Disk[{0, 0}, 1]}]',
        ),
        (
            "Compile[{x},Sqrt[x]]==2 + 3*a",
            "Compile[{x},Sqrt[x]] == 2 + 3*a",
        ),
        (
            "Compile[{x},Sqrt[x]]==Infinity",
            "Compile[{x},Sqrt[x]] == Infinity",
        ),
        (
            "Compile[{x},Sqrt[x]]==-Infinity",
            "Compile[{x},Sqrt[x]] == -Infinity",
        ),
        (
            "Compile[{x},Sqrt[x]]==Sqrt[I] Infinity",
            "Compile[{x},Sqrt[x]] == Times[Power[I,1/2],DirectedInfinity[1]]",
        ),
        (
            "Compile[{x},Sqrt[x]]==a",
            "Compile[{x},Sqrt[x]] == a",
        ),
        (
            'Compile[{x},Sqrt[x]]=="a"',
            'Compile[{x},Sqrt[x]]=="a"',
        ),
        (
            'Compile[{x},Sqrt[x]]=="1/4"',
            'Compile[{x},Sqrt[x]]=="1/4"',
        ),
        (
            "Compile[{x},Sqrt[x]]==I",
            "Compile[{x},Sqrt[x]]==I",
        ),
        (
            "Compile[{x},Sqrt[x]]==0",
            "Compile[{x},Sqrt[x]]==0",
        ),
        (
            "Compile[{x},Sqrt[x]]==0",
            "Compile[{x},Sqrt[x]]==0",
        ),
        (
            "Compile[{x},Sqrt[x]]==.25",
            "Compile[{x},Sqrt[x]]==.25",
        ),
        (
            "Compile[{x},Sqrt[x]]==Sqrt[2]",
            "Compile[{x},Sqrt[x]]==Sqrt[2]",
        ),
        (
            "Compile[{x},Sqrt[x]]==BesselJ[0,2]",
            "Compile[{x},Sqrt[x]]==BesselJ[0,2]",
        ),
        (
            "Compile[{x},Sqrt[x]]==3+2 I",
            "Compile[{x},Sqrt[x]]==3+2 I",
        ),
        (
            "Compile[{x},Sqrt[x]]==2.+ Pi I",
            "Compile[{x},Sqrt[x]]==2.+ Pi I",
        ),
        (
            "Compile[{x},Sqrt[x]]==3+Pi I",
            "Compile[{x},Sqrt[x]]==3+Pi I",
        ),
        (
            'Compile[{x},Sqrt[x]]==StringStream["Tengo una vaca lechera"]',
            'Compile[{x},Sqrt[x]]==StringStream["Tengo una vaca lechera"]',
        ),
        ("Compile[{x},Sqrt[x]]==Compile[{x},Sqrt[x]]", "True"),
        (
            "Compile[{x},Sqrt[x]]==Graphics[{Disk[{0,0},1]}]",
            "Compile[{x},Sqrt[x]]==Graphics[{Disk[{0,0},1]}]",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==2 + 3*a",
            "Graphics[{Disk[{0, 0}, 1]}] == 2 + 3*a",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==Infinity",
            "Graphics[{Disk[{0, 0}, 1]}] == Infinity",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==-Infinity",
            "Graphics[{Disk[{0, 0}, 1]}] == -Infinity",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==Sqrt[I] Infinity",
            "Graphics[{Disk[{0, 0}, 1]}] == Times[Power[I,1/2],DirectedInfinity[1]]",
        ),
        ("Graphics[{Disk[{0,0},1]}]==a", "Graphics[{Disk[{0, 0}, 1]}] == a"),
        ('Graphics[{Disk[{0,0},1]}]=="a"', "Graphics[{Disk[{0, 0}, 1]}] == \"a\""),
        ('Graphics[{Disk[{0,0},1]}]=="1/4"', "Graphics[{Disk[{0, 0}, 1]}] == \"1/4\""),
        ("Graphics[{Disk[{0,0},1]}]==I", "Graphics[{Disk[{0, 0}, 1]}] == I"),
        ("Graphics[{Disk[{0,0},1]}]==0", "Graphics[{Disk[{0, 0}, 1]}] == 0"),
        ("Graphics[{Disk[{0,0},1]}]==1/4", "Graphics[{Disk[{0, 0}, 1]}] == 1/4"),
        ("Graphics[{Disk[{0,0},1]}]==.25", "Graphics[{Disk[{0, 0}, 1]}] == 0.25"),
        (
            "Graphics[{Disk[{0,0},1]}]==Sqrt[2]",
            "Graphics[{Disk[{0, 0}, 1]}] == Sqrt[2]",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==BesselJ[0,2]",
            "Graphics[{Disk[{0, 0}, 1]}] == BesselJ[0, 2]",
        ),
        ("Graphics[{Disk[{0,0},1]}]==3+2 I", "Graphics[{Disk[{0, 0}, 1]}] == 3 + 2*I"),
        (
            "Graphics[{Disk[{0,0},1]}]==2.+ Pi I",
            "Graphics[{Disk[{0, 0}, 1]}] == 2. + 3.141592653589793*I",
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==3+Pi I",
            "Graphics[{Disk[{0, 0}, 1]}] == 3 + I*Pi",
        ),
        (
            'Graphics[{Disk[{0,0},1]}]==StringStream["Tengo una vaca lechera"]',
            'Graphics[{Disk[{0,0},1]}]==StringStream["Tengo una vaca lechera"]',
        ),
        (
            "Graphics[{Disk[{0,0},1]}]==Compile[{x},Sqrt[x]]",
            "Graphics[{Disk[{0,0},1]}]==Compile[{x},Sqrt[x]]",
        ),
        ("2 + 3*a==3+Pi I", "2 + 3*a == 3 + I*Pi"),
        ("2 + 3*a==2 + 3*a", "True",),
        ("2 + 3*a==Infinity", "2 + 3*a == Infinity",),
        ("2 + 3*a==-Infinity", "2 + 3*a == -Infinity",),
        (
            "2 + 3*a==Sqrt[I] Infinity",
            "2 + 3*a == DirectedInfinity[(-1)^(1/4)]",
        ),
        ("2 + 3*a==a", "2 + 3*a == a"),
        ('2 + 3*a=="a"', '2 + 3*a == "a"'),
        ('2 + 3*a=="1/4"', '2 + 3*a == "1/4"'),
        ("2 + 3*a==I", "2 + 3*a == I"),
        ("2 + 3*a==0", "2 + 3*a == 0"),
        ("2 + 3*a==1/4", "2 + 3*a == 1/4"),
        ("2 + 3*a==.25", "2 + 3*a == 0.25"),
        ("2 + 3*a==Sqrt[2]", "2 + 3*a == Sqrt[2]"),
        ("Graphics[{Disk[{0,0},1]}]==Graphics[{Disk[{0,0},1]}]", "True"),
        ("I == I", "True",),
        ("I == 0", "False",),
        ("I + 0 == 1 I - 0", "True",),
        ("I + 5 == I", "False",),
    ],
)
def test_cmp1_pass(str_expr, str_expected):
    check_evaluation(str_expr, str_expected)
