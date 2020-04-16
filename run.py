#! /usr/bin/env python
import benchml
import optparse
import json
log = benchml.log

def main(args):
    # Load datasets (as iterator)
    data = benchml.data.compile(
        filter_fct=benchml.filters[args.filter])
    # Compile models
    models = benchml.models.compile()
    # Evaluate
    bench = benchml.benchmark.evaluate(data, models, log)
    json.dump(bench, open(args.output, "w"), indent=1, sort_keys=True)

if __name__ == "__main__":
    parser = optparse.OptionParser()
    parser.add_option("-f", "--filter", dest="filter", default="none", 
        help="Dataset filter", metavar="F")
    parser.add_option("-o", "--output", dest="output", default="bench.json", 
        help="Output benchmark json file", metavar="J")
    args, _ = parser.parse_args()
    main(args)

