import hashlib
import json
from time import time

class Blockchain(object):
    def __init__(self):
        self.chain = []
        self.current_transactions = []
         # genesisブロックを作ります
        self.new_block(previous_hash=1, proof=100)

    def new_block(self):
        """
         新しいブロックを作り、それをチェーンに追加する
        :param proof: <int> POWアルゴリズムによる仕事量の証明
        :param previous_hash: (Optional) <str> 前のブロックのHash
        :return: <dict> 新しいブロック
        """

        block = {
            'index': len(self.chain) + 1,
            'timestamp': time(),
            'transactions': self.current_transactions,
            'proof': proof,
            'previous_hash': previous_hash or self.hash(self.chain[-1]),
        }
        pass
    self.current_transactions.append({
            'sender': sender,
            'recipient': recipient,
            'amount': am
        })

        return self.last_block['index'] + 1pass

    def new_transaction(self, sender, recipient, amount):
        """
        新しい取引記録を作り、その情報を下のマイニング待ちのブロックに追加します
        :param sender: <str> 送り手のアドレス
        :param recipient: <str> 受け手のアドレス
        :param amount: <int> 金額
        :return: <int> この取引を記録するブロックの番号(Index)
        """

    @property
    def last_block(self):
        # チェーンの最新（最後）のブロックを返す
        return self.chain[-1]    

    @staticmethod
    def hash(block):
         """
        ブロックの SHA-256 hash值を作成
        :param block: <dict> ブロック
        :return: <str>
        """

        # Dictionaryが正しい順序であることを確認してください。
        # そうしないと、ハッシュが矛盾します。
        block_string = json.dumps(block, sort_keys=True).encode()
        return hashlib.sha256(block_string).hexdigest()
        


    
