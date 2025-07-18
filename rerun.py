"""Rerun a robot with given body and parameters."""

import logging
import pickle

from evaluator import Evaluator
from individual import Individual

from revolve2.experimentation.logging import setup_logging

# This is a pickled genotype we optimized.
# You can copy your own parameters from the optimization output log.
PICKLED_GENOTYPE = b'\x80\x04\x95\x7f\x13\x00\x00\x00\x00\x00\x00\x8c\nindividual\x94\x8c\nIndividual\x94\x93\x94)\x81\x94}\x94(\x8c\x08genotype\x94h\x05\x8c\x08Genotype\x94\x93\x94)\x81\x94}\x94(\x8c\x05brain\x94\x8cGrevolve2.standards.genotypes.cppnwin._multineat_genotype_pickle_wrapper\x94\x8c\x1eMultineatGenotypePickleWrapper\x94\x93\x94)\x81\x94X\xf2\x08\x00\x00{\n"value0":{\n"value0":0,\n"value1":[\n{\n"value0":{\n"value0":[]\n},\n"value1":1,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":2,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":3,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":4,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":5,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":6,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":7,\n"value2":2,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":8,\n"value2":4,\n"value3":3.025,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":9,\n"value10":1.0\n}\n],\n"value2":[\n{\n"value0":{\n"value0":[]\n},\n"value1":1,\n"value2":8,\n"value3":1,\n"value4":false,\n"value5":0.10077116301569242\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":2,\n"value2":8,\n"value3":2,\n"value4":false,\n"value5":0.04286955232234167\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":3,\n"value2":8,\n"value3":3,\n"value4":false,\n"value5":-0.2003929017269797\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":4,\n"value2":8,\n"value3":4,\n"value4":false,\n"value5":-0.16672455726949426\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":5,\n"value2":8,\n"value3":5,\n"value4":false,\n"value5":0.554556936309183\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":6,\n"value2":8,\n"value3":6,\n"value4":false,\n"value5":-0.7692001390199259\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":7,\n"value2":8,\n"value3":7,\n"value4":false,\n"value5":-0.5891041915543674\n}\n],\n"value3":7,\n"value4":1,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0.0,\n"value9":false,\n"value10":16384,\n"value11":{\n"value0":[]\n},\n"value12":8,\n"value13":7\n}\n}\x94b\x8c\x04body\x94h\r)\x81\x94X\xa1\t\x00\x00{\n"value0":{\n"value0":0,\n"value1":[\n{\n"value0":{\n"value0":[]\n},\n"value1":1,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":2,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":3,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":4,\n"value2":1,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":5,\n"value2":2,\n"value3":0.0,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":1,\n"value10":0.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":6,\n"value2":4,\n"value3":3.025,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":10,\n"value10":1.0\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":7,\n"value2":4,\n"value3":3.025,\n"value4":0.0,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0,\n"value9":10,\n"value10":1.0\n}\n],\n"value2":[\n{\n"value0":{\n"value0":[]\n},\n"value1":1,\n"value2":6,\n"value3":1,\n"value4":false,\n"value5":0.8269418786610535\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":2,\n"value2":6,\n"value3":2,\n"value4":false,\n"value5":0.5879881043408579\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":3,\n"value2":6,\n"value3":3,\n"value4":false,\n"value5":-0.17822091751068853\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":4,\n"value2":6,\n"value3":4,\n"value4":false,\n"value5":-0.92174205740244\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":5,\n"value2":6,\n"value3":5,\n"value4":false,\n"value5":-0.5153398692350166\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":1,\n"value2":7,\n"value3":6,\n"value4":false,\n"value5":0.5894387671212202\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":2,\n"value2":7,\n"value3":7,\n"value4":false,\n"value5":-0.2611333435218285\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":3,\n"value2":7,\n"value3":8,\n"value4":false,\n"value5":0.2472344139941804\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":4,\n"value2":7,\n"value3":9,\n"value4":false,\n"value5":-0.8978891030596082\n},\n{\n"value0":{\n"value0":[]\n},\n"value1":5,\n"value2":7,\n"value3":10,\n"value4":false,\n"value5":0.998396361957343\n}\n],\n"value3":5,\n"value4":2,\n"value5":0.0,\n"value6":0.0,\n"value7":0,\n"value8":0.0,\n"value9":false,\n"value10":16384,\n"value11":{\n"value0":[]\n},\n"value12":7,\n"value13":10\n}\n}\x94bub\x8c\x07fitness\x94G?\xfaO\x96\x1a#\x89\xc1ub.'


def main() -> None:
    """Perform the rerun."""
    setup_logging()

    individual: Individual = pickle.loads(PICKLED_GENOTYPE)

    logging.info(f"Fitness from pickle: {individual.fitness}")

    evaluator = Evaluator(
        headless=False,
        num_simulators=1,
    )
    fitness = evaluator.evaluate([individual.genotype])[0]
    logging.info(f"Rerun fitness: {fitness}")


if __name__ == "__main__":
    main()
