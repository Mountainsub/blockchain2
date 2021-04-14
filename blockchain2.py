import hashlib
import json

from time import time
from uuid import uuid4


class Blockchain(object):
    ...

    def proof_of_work(self, last_proof):
        """
        簡単なPOW:
         - 始めの4つの数字が0になるhash(pp')を使ってp' 値を求めましょう
         - p とは前のブロックの証明でp'とは現在のブロックの証明です
        :param last_proof: <int>
        :return: <int>
        """

        proof = 0
        while self.valid_proof(last_proof, proof) is False:
            proof += 1

        return proof

    @staticmethod
    def valid_proof(last_proof, proof):
        """
        検証を証明する: hash(last_proof, proof)は0000から始まるか？
        :param last_proof: <int> 前のブロックの証明
        :param proof: <int> 現在のブロックの証明
        :return: <bool> もし正しいならTrue、誤りならFalseを返す
        """

        guess = f'{last_proof}{proof}'.encode()
        guess_hash = hashlib.sha256(guess).hexdigest()
        return guess_hash[:4] == "0000"