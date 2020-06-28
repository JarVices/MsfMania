from lib import core, evasion
from random import randrange, randint


def junk_inject(junk, method, intensity):
    funcname = ""
    func = ""
    code = ""

    if junk == "yes":
        number = 0
        if method == "code":
            number += randint(4, 8)
        else:
            number += randint(64, 128)
        injection = 0
        while injection != number:
            injection += 1
            H = intensity
            random_func = randint(1, 52)
            funccode = ""
            if random_func == 1:
                funccode += sum_first_n_integer_1(H)

            elif random_func == 2:
                funccode += sum_first_n_inter_2(H)

            elif random_func == 3:
                funccode += fibonacci(H)

            elif random_func == 4:
                funccode += twin_tower(H)

            elif random_func == 5:
                funccode += back_to_zero(H)

            elif random_func == 6:
                funccode += back_to_num_1(H)

            elif random_func == 7:
                funccode += back_to_num_2(H)

            elif random_func == 8:
                funccode += primes_number_soe(H)

            elif random_func == 9:
                funccode += primes_number_sos(H)

            elif random_func == 10:
                funccode += average_1(H)

            elif random_func == 11:
                funccode += average_2(H)

            elif random_func == 12:
                funccode += average_variance_stanard_and_deviation_1(H)

            elif random_func == 13:
                funccode += average_variance_stanard_and_deviation_2(H)

            elif random_func == 14:
                funccode += reverse_array_1(H)

            elif random_func == 15:
                funccode += reverse_array_2(H)

            elif random_func == 16:
                funccode += double_reverse_array_1(H)

            elif random_func == 17:
                funccode += double_reverse_array_2(H)

            elif random_func == 18:
                funccode += random_numbers(H)

            elif random_func == 19:
                funccode += buble_sort_int_array(H)

            elif random_func == 20:
                funccode += buble_sort_float_array(H)

            elif random_func == 21:
                funccode += gnome_sort_int_array(H)

            elif random_func == 22:
                funccode += last_armstrong(H)

            elif random_func == 23:
                funccode += odd_or_even_1(H)

            elif random_func == 24:
                funccode += odd_or_even_2(H)

            elif random_func == 25:
                funccode += ceil_routine_1(H)

            elif random_func == 26:
                funccode += ceil_routine_2(H)

            elif random_func == 27:
                funccode += floor_routine_1(H)

            elif random_func == 28:
                funccode += floor_routine_2(H)

            elif random_func == 29:
                funccode += acos_routine_1(H)

            elif random_func == 30:
                funccode += acos_routine_2(H)

            elif random_func == 31:
                funccode += asin_routine_1(H)

            elif random_func == 32:
                funccode += asin_routine_2(H)

            elif random_func == 33:
                funccode += atan_routine_1(H)

            elif random_func == 34:
                funccode += atan_routine_2(H)

            elif random_func == 35:
                funccode += fabs_routine_1(H)

            elif random_func == 36:
                funccode += fabs_routine_2(H)

            elif random_func == 37:
                funccode += exp_routine_1(H)

            elif random_func == 38:
                funccode += exp_routine_2(H)

            elif random_func == 39:
                funccode += ln_routine_1(H)

            elif random_func == 40:
                funccode += ln_routine_2(H)

            elif random_func == 41:
                funccode += log10_routine_1(H)

            elif random_func == 42:
                funccode += log10_routine_2(H)

            elif random_func == 43:
                funccode += fmod_routine_1(H)

            elif random_func == 44:
                funccode += fmod_routine_2(H)

            elif random_func == 45:
                funccode += ldexp_routine_1(H)

            elif random_func == 46:
                funccode += ldexp_routine_2(H)

            elif random_func == 47:
                funccode += geometric_1(H)

            elif random_func == 48:
                funccode += geometric_2(H)

            elif random_func == 49:
                funccode += geometric_3(H)

            elif random_func == 50:
                funccode += geometric_4(H)

            elif random_func == 51:
                funccode += geometric_5(H)

            elif random_func == 52:
                funccode += shaker_snort(H)

            if method == "code":
                code += funccode

            else:
                evasion_funcname = "void " + core.varname_creator() + "(void)\n"
                func += evasion_funcname
                func += "{\n"
                func += funccode
                func += "}\n"
                funcname += evasion.replace_string(evasion_funcname)

        if method == "code":
            return code
        else:
            return funcname, func

    else:
        if method == "code":
            return ""
        else:
            return "", ""



def sum_first_n_integer_1(H):
    randcounter = core.varname_creator()
    randcounter2 = core.varname_creator()
    randcounter3 = core.varname_creator()
    randbignumb = str(randint(10 * H, 99 * H))
    junkcode = "int " + randcounter + "," + randcounter2 + ";\n"
    junkcode += "unsigned long long int " + randcounter3 + " = 0;\n"
    junkcode += randcounter2 + " = " + randbignumb + ";\n"
    junkcode += "for (" + randcounter + " = 1; " + randcounter + " <= " + randcounter2 + "; " + randcounter + "++){\n"
    junkcode += randcounter3 + " = " + randcounter3 + "+" + randcounter + ";}\n"
    return junkcode


def sum_first_n_inter_2(H):
    randcounter = core.varname_creator()
    randcounter2 = core.varname_creator()
    randbignumb = str(randint(10 * H, 99 * H))
    junkcode = "int " + randcounter + ";\n"
    junkcode += "unsigned long long int " + randcounter2 + " = 0;\n"
    junkcode += randcounter + " = " + randbignumb + ";\n"
    junkcode += "while(" + randcounter + " > 0){\n"
    junkcode += randcounter2 + " = " + randcounter2 + "+" + randcounter + ";\n"
    junkcode += randcounter + " = " + randcounter + " - 1;}\n"
    return junkcode


def fibonacci(H):
    rand1 = core.varname_creator()
    rand2 = core.varname_creator()
    rand3 = core.varname_creator()
    rand4 = core.varname_creator()
    rand5 = core.varname_creator()
    randbignumb = str(randint(10 * H, 99 * H))
    junkcode = "int " + rand1 + " = 0," + rand2 + " = 1," + rand3 + "," + rand4 + "," + rand5 + " = 0;\n"
    junkcode += rand4 + " = " + randbignumb + ";\n"
    junkcode += "while (" + rand5 + " < " + rand4 + "){\n"
    junkcode += rand3 + " = " + rand1 + " + " + rand2 + ";\n" + rand5 + "++;\n"
    junkcode += rand1 + "=" + rand2 + ";\n" + rand2 + " = " + rand3 + ";}\n"
    return junkcode


def twin_tower(H):
    randbig1 = str(randrange(10 * H, 99 * H, 10))
    randbig2 = str(randrange(10 * H, 77 * H, 10))
    randcpt = core.varname_creator()
    randcpt2 = core.varname_creator()
    junkcode = "int " + randcpt + "  = " + randbig1 + ";\n"
    junkcode += "int " + randcpt2 + " = " + randbig2 + ";\n"
    junkcode += "while ( " + randcpt + " > 0 ){\n"
    junkcode += "if (" + randcpt + " > " + randcpt2 + "){\n"
    junkcode += randcpt + " = " + randcpt + " - 1;\n"
    junkcode += "}else{\n"
    junkcode += randcpt2 + " = " + randcpt2 + " - 1;}}\n"
    return junkcode


def back_to_zero(H):
    randbig1 = str(randrange(10 * H, 99 * H, 10))
    randcpt = core.varname_creator()
    junkcode = "int " + randcpt + "  = " + randbig1 + ";\n"
    junkcode += "while ( " + randcpt + " > 0 ){\n"
    junkcode += randcpt + " = " + randcpt + " - 1;}\n"
    return junkcode


def pow_counter(H):
    randsmall = str(uniform(1.000001000, 1.000003000))
    randsmall2 = str(uniform(1.000001000, 1.000003000))
    randbig = str(randrange(10 * H, 99 * H, 10))
    randcpt = core.varname_creator()
    randi = core.varname_creator()
    junkcode = "double " + randcpt + "  = " + randsmall + ";\n"
    junkcode += "double " + randi + " = " + randsmall2 + ";\n"
    junkcode += "while(" + randcpt + " < " + randbig + "){\n"
    junkcode += randcpt + " = pow(" + randcpt + "," + randi + ");}\n"
    return junkcode


def back_to_num_1(H):
    randbig1 = str(randrange(10 * H, 99 * H, 10))
    randcpt = core.varname_creator()
    junkcode = "int " + randcpt + "  = " + randbig1 + ";\n"
    junkcode += "while ( " + randcpt + " > " + str(randrange(10, 99, 2)) + " ){\n"
    junkcode += randcpt + " = " + randcpt + " - 1;}\n"
    return junkcode


def back_to_num_2(H):
    randbig1 = str(randrange(10 * H, 99 * H, 10))
    randcpt = core.varname_creator()
    randcpt2 = core.varname_creator()
    junkcode = "int " + randcpt + ";\n"
    junkcode += "int " + randcpt2 + " = " + randbig1 + ";\n"
    junkcode += "for(" + randcpt + " = " + randbig1 + ";" + randcpt + " > " + str(randrange(10, 99, 2)) + ";" + randcpt + "--){\n"
    junkcode += randcpt2 + " = " + randcpt2 + " - 1;}\n"
    return junkcode


def primes_number_sos(H):
    randarraysize = core.varname_creator()
    randranges = str(randint(10 * H, 99 * H))
    randprimevar = core.varname_creator()
    randprimenumb = core.varname_creator()
    randsizevar = core.varname_creator()
    isprime = core.varname_creator()
    randn = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int " + randflag + "," + randflag2 + ";\n"
    junkcode += "int " + randprimevar + " = 0;\n"
    junkcode += "int " + randarraysize + " = " + randranges + ";\n"
    junkcode += "int " + randn + " = " + randranges + " / 2;\n"
    junkcode += "int " + randsizevar + ";\n"
    junkcode += "int* " + isprime + " = (int*)malloc(sizeof(int) * (" + randarraysize + " + 1));\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randn + ";" + randflag + "++){\n"
    junkcode += isprime + "[" + randflag + "] = " + randflag + ";}\n"
    junkcode += "for(" + randflag + " = 1;" + randflag + " < " + randn + ";" + randflag + "++){\n"
    junkcode += "for(" + randflag2 + " = " + randflag + ";" + randflag2 + " <= (" + randn + " - " + randflag + ")/(2 * " + randflag + " + 1);" + randflag2 + "++){\n"
    junkcode += isprime + "[" + randflag + " + " + randflag2 + " + 2 * " + randflag + " + " + randflag2 + "] = 0;}}\n"
    junkcode += "if(" + randarraysize + " > 2){\n"
    junkcode += isprime + "[" + randprimevar + "++] = 2;}\n"
    junkcode += "for(" + randflag + " = 1;" + randflag + " < " + randn + ";" + randflag + "++){\n"
    junkcode += "if(" + isprime + "[" + randflag + "] != 0){\n"
    junkcode += isprime + "[" + randprimevar + "++] = " + randflag + " * 2 + 1;}}\n"
    junkcode += randsizevar + " = sizeof " + isprime + " / sizeof(int);\n"
    junkcode += "int " + randprimenumb + " = 0;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randsizevar + ";" + randflag + "++){\n"
    junkcode += "if(" + isprime + "[" + randflag + "] != 0){\n"
    junkcode += randprimenumb + " ++;}}\n"
    junkcode += "free(" + isprime + ");\n"
    return junkcode


def primes_number_soe(H):
    randranges = str(randint(10 * H, 99 * H))
    randprimevar = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "unsigned long long int " + randflag + "," + randflag2 + ";\n"
    junkcode += "int *" + randprimevar + ";\n"
    junkcode += "int " + randvar + " = 1;\n"
    junkcode += randprimevar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "for(" + randflag + " = 2;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randprimevar + "[" + randflag + "] = 1;}\n"
    junkcode += "for(" + randflag + " = 2;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += "if(" + randprimevar + "[" + randflag + "]){\n"
    junkcode += "for(" + randflag2 + " = " + randflag + ";" + randflag + " * " + randflag2 + " < " + randranges + ";" + randflag2 + "++){\n"
    junkcode += randprimevar + "[" + randflag + " * " + randflag2 + "] = 0;}}}\n"
    junkcode += "free(" + randprimevar + ");\n"
    return junkcode


def average_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;\n"
    junkcode += "float " + randaverage + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 30;}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}\n"
    junkcode += randaverage + "/((float)" + randranges + ");\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def average_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "float " + randaverage + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 25;\n"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}\n"
    junkcode += randaverage + "/((float)" + randranges + ");\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def average_variance_stanard_and_deviation_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvariance = core.varname_creator()
    randdevstd = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "int " + randsum + " = 0;int " + randsum2 + " = 0;\n"
    junkcode += "float " + randaverage + "," + randvariance + "," + randdevstd + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 35;}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}\n"
    junkcode += randaverage + "/((float)" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randsum2 + " = " + randsum2 + " + pow((" + randvar + "[" + randflag + "]" + " - " + randaverage + "),2);}\n"
    junkcode += randvariance + " = " + randsum2 + "/((float)" + randranges + ");\n"
    junkcode += randdevstd + " = sqrt(" + randvariance + ");\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def average_variance_stanard_and_deviation_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randsum2 = core.varname_creator()
    randaverage = core.varname_creator()
    randvariance = core.varname_creator()
    randdevstd = core.varname_creator()
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randsum + " = 0;int " + randsum2 + " = 0;\n"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "float " + randaverage + "," + randvariance + "," + randdevstd + ";\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 35;\n"
    junkcode += randsum + " = " + randsum + " + " + randvar + "[" + randflag + "];}\n"
    junkcode += randaverage + "/((float)" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randsum2 + " = " + randsum2 + " + pow((" + randvar + "[" + randflag + "]" + " - " + randaverage + "),2);}\n"
    junkcode += randvariance + " = " + randsum2 + "/((float)" + randranges + ");\n"
    junkcode += randdevstd + " = sqrt(" + randvariance + ");\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def reverse_array_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randflag = core.varname_creator()
    randlenght = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randlenght + " = " + randranges + " - 1;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randlenght + "];\n"
    junkcode += randlenght + " = " + randlenght + " - 1;}\n"
    junkcode += "free(" + randvar + ");free(" + randrevvar + ");\n"
    return junkcode


def reverse_array_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;\n"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];\n"
    junkcode += randLenght + " = " + randLenght + " - 1;}\n"
    junkcode += "free(" + randvar + ");free(" + randrevvar + ");\n"
    return junkcode


def double_reverse_array_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randrevvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;\n"
    junkcode += randvar2 + "[" + randflag + "] = rand() % 300;}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];\n"
    junkcode += randrevvar2 + "[" + randflag + "] = " + randvar2 + "[" + randLenght + "];\n"
    junkcode += randLenght + " = " + randLenght + " - 1;}\n"
    junkcode += "free(" + randvar + ");free(" + randvar2 + ");free(" + randrevvar + ");free(" + randrevvar2 + ");\n"
    return junkcode


def double_reverse_array_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randrevvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randrevvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randLenght = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int* " + randvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int* " + randrevvar2 + " = (int*)malloc(sizeof(int) * " + randranges + ");\n"
    junkcode += "int " + randLenght + " = " + randranges + " - 1;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 300;\n"
    junkcode += randvar2 + "[" + randflag + "] = rand() % 300;\n"
    junkcode += randrevvar + "[" + randflag + "] = " + randvar + "[" + randLenght + "];\n"
    junkcode += randrevvar2 + "[" + randflag + "] = " + randvar2 + "[" + randLenght + "];\n"
    junkcode += randLenght + " = " + randLenght + " - 1;}\n"
    junkcode += "free(" + randvar + ");free(" + randvar2 + ");free(" + randrevvar + ");free(" + randrevvar2 + ");\n"
    return junkcode


def random_numbers(H):
    randranges = str(randint(10 * H, 99 * H))
    randvarr = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int " + randflag + "," + randflag2 + " = 0;\n"
    junkcode += "float* " + randvarr + " = (float*)malloc(sizeof(float) * " + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randflag2 + " = rand() % 400;\n"
    junkcode += "if(" + randflag2 + " > 360){\n"
    junkcode += randvarr + "[" + randflag + "] = 0;\n"
    junkcode += "}else if(" + randflag2 + " < 0){\n"
    junkcode += randvarr + "[" + randflag + "] = 0;\n"
    junkcode += "}else{\n"
    junkcode += randvarr + "[" + randflag + "] = " + randflag2 + " * 0.1 / 360;\n}}"
    junkcode += "free(" + randvarr + ");\n"
    return junkcode


def buble_sort_int_array(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "int " + randflag2 + ";\n"
    junkcode += "int " + randvar2 + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000 ;}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += "for(" + randflag2 + " = 0;" + randflag2 + " < (" + randranges + " - " + randflag + " - 1);" + randflag + "++){\n"
    junkcode += "if(" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag2 + " + 1]){"
    junkcode += randvar2 + " = " + randvar + "[" + randflag2 + "];\n"
    junkcode += randvar + "[" + randflag2 + "] = " + randvar + "[" + randflag + " + 1];\n"
    junkcode += randvar + "[" + randflag2 + " + 1] = " + randvar2 + ";}}}\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def buble_sort_float_array(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    junkcode = "float *" + randvar + " = (float*)malloc(sizeof(float)*" + randranges + ");\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "int " + randflag2 + ";\n"
    junkcode += "float " + randvar2 + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (float)(rand() % 1000) / (float)(rand() % 70);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += "for(" + randflag2 + " = 0;" + randflag2 + " < (" + randranges + " - " + randflag + " - 1);" + randflag + "++){\n"
    junkcode += "if(" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag2 + " + 1]){"
    junkcode += randvar2 + " = " + randvar + "[" + randflag2 + "];\n"
    junkcode += randvar + "[" + randflag2 + "] = " + randvar + "[" + randflag + " + 1];\n"
    junkcode += randvar + "[" + randflag2 + " + 1] = " + randvar2 + ";}}}\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def gnome_sort_int_array(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randtemp = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "int " + randtemp + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000;}\n"
    junkcode += randflag + "=0;\n"
    junkcode += "while(" + randflag + " < " + randranges + "){\n"
    junkcode += "if(" + randflag + " == 0 || " + randvar + "[" + randflag + "-1] <= " + randvar + "[" + randflag + "]){\n"
    junkcode += randflag + "++;\n"
    junkcode += "}else{\n"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "-1];\n"
    junkcode += randvar + "[" + randflag + "-1] = " + randvar + "[" + randflag + "];\n"
    junkcode += randvar + "[" + randflag + "] = " + randtemp + ";\n"
    junkcode += randflag + " = " + randflag + "-1;}}\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def last_armstrong(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    randLastArmN = core.varname_creator()
    junkcode = "int " + randLastArmN + ";\n"
    junkcode += "int " + randvar + "," + randflag + "," + randvar2 + "," + randflag2 + ";\n"
    junkcode += "for(" + randflag + " = 1;" + randflag + " <= " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + " = 0;\n"
    junkcode += randvar2 + " = " + randflag + ";\n"
    junkcode += "while(" + randvar2 + " != 0){\n"
    junkcode += randflag2 + " = " + randvar2 + "%10;\n"
    junkcode += randvar + " += " + randflag2 + "*" + randflag2 + "*" + randflag2 + ";\n"
    junkcode += randvar2 + " = " + randvar2 + "/10;}\n"
    junkcode += "if(" + randvar + " == " + randflag + "){\n"
    junkcode += randLastArmN + " = " + randflag + ";}}\n"
    return junkcode


def odd_or_even_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randodd = core.varname_creator()
    randeven = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "int " + randodd + " = 0;\n"
    junkcode += "int " + randeven + " = 0;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 100000;}\n"
    junkcode += randflag + " = " + "0;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += "if(" + randvar + "[" + randflag + "]&1){\n"
    junkcode += randodd + " += 1;\n"
    junkcode += "}else if(!(" + randvar + "[" + randflag + "]&1)){\n"
    junkcode += randeven + " += 1;}}\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def odd_or_even_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randodd = core.varname_creator()
    randeven = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "int " + randodd + " = 0;\n"
    junkcode += "int " + randeven + " = 0;\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 1000;\n"
    junkcode += "if(" + randvar + "[" + randflag + "]&1){\n"
    junkcode += randodd + " += 1;\n"
    junkcode += "}else if(!(" + randvar + "[" + randflag + "]&1)){\n"
    junkcode += randeven + " += 1;}}\n"
    junkcode += "free(" + randvar + ");\n"
    return junkcode


def ceil_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def ceil_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + " = -1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);\n"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def floor_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar2 + "[" + randflag + "] = floor(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def floor_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randvar2 = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + " = -1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "double *" + randvar2 + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = (double)(rand() % 1000) / (double)(rand() % 70);\n"
    junkcode += randvar2 + "[" + randflag + "] = ceil(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def acos_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = acos(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def acos_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);\n"
    junkcode += randvar + "[" + randflag + "] = acos(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def asin_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randflag = core.varname_creator()
    randvar = core.varname_creator()

    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = asin(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def asin_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);\n"
    junkcode += randvar + "[" + randflag + "] = asin(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def atan_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = atan(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def atan_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));\n"
    junkcode += randvar + "[" + randflag + "] = atan(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def fabs_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = fabs(" + randvar + "[" + randflag + "]);}\n"
    return junkcode


def fabs_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = (double)((2*(rand() / (double)(RAND_MAX))) - (double)1);\n"
    junkcode += randvar + "[" + randflag + "] = fabs(" + randvar + "[" + randflag + "]);}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def exp_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + " = exp((double)(" + str(randint(2, 10)) + "*rand() / (double)(RAND_MAX)));}\n"
    return junkcode


def exp_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + " = exp((double)(" + str(randint(2, 10)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def ln_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}\n"
    return junkcode


def ln_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def log10_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}\n"
    return junkcode


def log10_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + " = log((double)(" + str(randint(20, 1000)) + "*rand() / (double)(RAND_MAX)));}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def fmod_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));}\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = fmod(" + randvar + "[" + randflag + "],(double)(rand() % 100));}\n"
    return junkcode


def fmod_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    junkcode = "int " + randflag + "=-1;\n"
    junkcode += "double *" + randvar + " = (double*)malloc(sizeof(double)*" + randranges + ");\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randvar + "[" + randflag + "] = ((double)rand() / (double)(RAND_MAX));\n"
    junkcode += randvar + "[" + randflag + "] = fmod(" + randvar + "[" + randflag + "],(double)(rand() % 100));}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def ldexp_routine_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randinteger = core.varname_creator()
    junkcode = "int " + randinteger + ";\n"
    junkcode += "int " + randflag + ";\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randinteger + " = rand() % " + str(randint(16, 32)) + ";\n"
    junkcode += randvar + " = ldexp((double)(rand() / (double)(RAND_MAX))," + randinteger + ");}\n"
    return junkcode


def ldexp_routine_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randvar = core.varname_creator()
    randflag = core.varname_creator()
    randinteger = core.varname_creator()
    junkcode = "int " + randinteger + ";\n"
    junkcode += "int " + randflag + "=-1;\n"
    junkcode += "double " + randvar + ";\n"
    junkcode += "do{\n"
    junkcode += randflag + "++;\n"
    junkcode += randinteger + " = rand() % " + str(randint(16, 32)) + ";\n"
    junkcode += randvar + " = ldexp((double)(rand() / (double)(RAND_MAX))," + randinteger + ");}while(" + randflag + " < " + randranges + "-1);\n"
    return junkcode


def geometric_1(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;\n"
    junkcode += "double " + randdiv + "=1;\n"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;\n"
    junkcode += randdiv + "=" + randdiv + "*2;\n"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");\n"
    junkcode += "if(" + randsum + " == 1.00)break;}\n"
    return junkcode


def geometric_2(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;\n"
    junkcode += "double " + randdiv + "=1;\n"
    junkcode += "int " + randflag + "=0;\n"
    junkcode += "do{\n"
    junkcode += randflag + " += 1;\n"
    junkcode += randdiv + "=" + randdiv + "* 2;\n"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");\n"
    junkcode += "if(" + randsum + " == 1.00)break;}while(" + randflag + " < " + randranges + ");\n"
    return junkcode


def geometric_3(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;\n"
    junkcode += "double " + randdiv + "=1;\n"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;\n"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");\n"
    junkcode += randdiv + " *= 4;\n"
    junkcode += "if(" + randsum + " == 1.33333333333333333333)break;}\n"
    return junkcode


def geometric_4(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;\n"
    junkcode += "double " + randdiv + "=1;\n"
    junkcode += "int " + randflag + "=0;\n"
    junkcode += "do{\n"
    junkcode += randflag + " += 1;\n"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");\n"
    junkcode += randdiv + "*=4;\n"
    junkcode += "if(" + randsum + " == 1.33333333333333333333)break;}while(" + randflag + " < " + randranges + ");\n"
    return junkcode


def geometric_5(H):
    randranges = str(randint(10 * H, 99 * H))
    randsum = core.varname_creator()
    randflag = core.varname_creator()
    randdiv = core.varname_creator()
    junkcode = "double " + randsum + "=0;\n"
    junkcode += "double " + randdiv + "=1;\n"
    junkcode += "for(int " + randflag + "=0;" + randflag + " < " + randranges + ";" + randflag + "++){;\n"
    junkcode += randdiv + " *= 4;\n"
    junkcode += randsum + " = " + randsum + " + (1 / " + randdiv + ");\n"
    junkcode += "if(" + randsum + " == 0.33333333333333333333)break;}\n"
    return junkcode


def shaker_snort(H):
    randranges = str(randint(10 * H, 99 * H))
    randflag = core.varname_creator()
    randflag2 = core.varname_creator()
    randtemp = core.varname_creator()
    randvar = core.varname_creator()
    junkcode = "int " + randflag + ";\n"
    junkcode += "int *" + randvar + " = (int*)malloc(sizeof(int)*" + randranges + ");\n"
    junkcode += "for(" + randflag + " = 0;" + randflag + " < " + randranges + ";" + randflag + "++){\n"
    junkcode += randvar + "[" + randflag + "] = rand() % 10000;}\n"
    junkcode += "int " + randflag2 + ";\n"
    junkcode += "int " + randtemp + ";\n"
    junkcode += "for (" + randflag2 + " = 1; " + randflag2 + " <= " + randranges + " / 2; " + randflag2 + "++){\n"
    junkcode += "for (" + randflag + " = " + randflag2 + " - 1; " + randflag + " < " + randranges + " - " + randflag2 + "; " + randflag + "++){\n"
    junkcode += "if (" + randvar + "[" + randflag + "] > " + randvar + "[" + randflag + "+1]){\n"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "];\n"
    junkcode += randvar + "[" + randflag + "] = " + randvar + "[" + randflag + "+1];\n"
    junkcode += randvar + "[" + randflag + "+1] = " + randtemp + ";}}\n"
    junkcode += "for (" + randflag + " = " + randranges + " - " + randflag2 + " - 1; " + randflag + " >= " + randflag2 + "; " + randflag + "--){\n"
    junkcode += "if (" + randvar + "[" + randflag + "] < " + randvar + "[" + randflag + "-1]){\n"
    junkcode += randtemp + " = " + randvar + "[" + randflag + "];\n"
    junkcode += randvar + "[" + randflag + "] = " + randvar + "[" + randflag + "-1];\n"
    junkcode += randvar + "[" + randflag + "-1] = " + randtemp + ";}}}\n"
    return junkcode
