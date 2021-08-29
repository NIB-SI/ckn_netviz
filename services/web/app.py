import os
import json
import networkx as nx

from flask import Flask, flash, g, redirect, render_template, request, session
from flask_cors import CORS, cross_origin

from . import utils


BASEDIR = os.path.dirname(__file__)
ckn = nx.read_gpickle(os.path.join(BASEDIR, 'data/LKN.pickle'))


def create_app(test_config=None):
    # create and configure the app
    app = Flask(__name__, instance_relative_config=True)
    CORS(app)
    app.config.from_mapping(
        SECRET_KEY='dev',
    )

    @app.route('/suggest')
    def suggest():
        text = request.args.get('term', '').strip()
        if not text:
            return {'results': []}
        # return {'results': [{'id': i, 'text': node} for i, node in enumerate(ckn.nodes)]}
        result = utils.best_matching_nodes(ckn, request.args.get('term', ''), k=10)
        return {'results': [{'id': i, 'text': node} for i, node in enumerate(result)]}

    @app.route('/extract_network', methods=['GET', 'POST'])
    def query_network():
        try:
            data = request.get_json(force=False)
            nodes = data.get('nodes')
        except Exception as e:
            return {'error': 'Invalid query data'}
        if len(nodes) == 0:
            return {'error': 'Empty input'}
        graph = utils.extract_subgraph(ckn, nodes, k=1, ignoreDirection=False, fuzzySearch=False)
        # graph = ckn.subgraph(nodes).copy()
        # for i, node in enumerate(graph.nodes):
        #     graph.nodes[node]['id'] = i+1
        return {'network': utils.graph2json(graph)}  # {'nodes': nlist, 'edges': elist}

    @app.route('/')
    @cross_origin()
    def main():
        return render_template('index.html')

    return app
