from common.logger import Logger
from neo4j import GraphDatabase
from parser.grammar import GrammarItem
import config


class Neo4jDatabase:
    def __init__(self):
        self.connection = GraphDatabase.driver(f"bolt://{config.NEO4J_HOST}", auth=(config.NEO4J_USER, config.NEO4J_PASSWORD))
        self.logger = Logger().logger
        self.logger.info("Neo4j ready to query")

    def close(self):
        self.connection.close()

    def create_node(self, rule: GrammarItem):
        query = """MERGE (node:RuleItem {type: rule.type_name, word: rule.word})"""
        with self.connection.session() as session:
            session.build_index(query, rule=rule)

    def create_connection(self, a: GrammarItem, b: GrammarItem):
        query = """
        MERGE (a:RuleItem {type: a.type_name, word: a.word});
        MERGE (b:RuleItem {type: b.type_name, word: b.word});
        MERGE (a)-[r:DEP {dep: a.token.dep_}]->(b)
        ON CREATE SET r.count = 1
        ON MATCH SET r.count = r.count + 1
        """
        with self.connection.session() as session:
            session.build_index(query, a=a, b=b)
