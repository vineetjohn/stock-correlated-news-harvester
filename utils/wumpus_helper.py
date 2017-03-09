import math

from utils import log_helper


def execute_wumpus_command(wumpus, command):
    """
    @Params: Wumpus telnet instance, Text command to run
    @Returns: Wumpus output
    """
    wumpus.write(command.encode("utf-8"))
    return wumpus.read_until(b"@0-Ok").decode("utf-8").strip().split("\n")


def extract_numeric_wumpus_response(response):
    """
    @Params: Wumpus output
    @Returns: First output line formatted as a number
    """
    for term in response:
        if term.strip().isdigit():
            numeric_value = int(term.strip())
            return numeric_value

    return 0


def calcMI(wumpus, term_1, term_2, collocation_span):
    """
    @Params: Wumpus telnet instance, terms (2 params), term collocation span
    @Returns: Normalized pointwise mutual index
    """

    log = log_helper.get_logger("wumpus_helper")
    corpus_term_frequency = 30230685715

    # get frequency of NP1
    command = "@count \"" + term_1.strip() + "\"\n"
    term_1_freq_response = execute_wumpus_command(wumpus, command)
    term_1_freq = extract_numeric_wumpus_response(term_1_freq_response)
    log.debug("TF1: " + str(term_1_freq))

    # get frequency of NP2
    command = "@count \"" + term_2.strip() + "\"\n"
    term_2_freq_response = execute_wumpus_command(wumpus, command)
    term_2_freq = extract_numeric_wumpus_response(term_2_freq_response)
    log.debug("TF2: " + str(term_2_freq))

    # get joint frequency
    command = \
        "@count (\"" + term_1 + "\" ^ \"" + term_2 + \
        "\") < [" + str(collocation_span) + "] < (\"<doc>\"..\"</doc>\") \n"
    joint_freq_response = execute_wumpus_command(wumpus, command)
    joint_freq = extract_numeric_wumpus_response(joint_freq_response)
    log.debug("JF: " + str(joint_freq))

    # calculate NPMI (normalised pointwise mutual information)
    mutual_information = 0
    prob_term_1 = term_1_freq / corpus_term_frequency
    prob_term_2 = term_2_freq / corpus_term_frequency
    joint_prob = joint_freq / corpus_term_frequency

    if joint_prob > 0 and prob_term_1 > 0 and prob_term_2 > 0:
        mutual_information = \
            math.log(joint_prob / (prob_term_1 * prob_term_2)) /\
            -math.log(joint_prob)

    return mutual_information
