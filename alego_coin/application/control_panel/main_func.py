from control_panel.util import coin_data_formatter, create_timestamp
from control_panel.cryptography_func import coin_data_hasher, validate_coin_data_hash, generate_random_id, generate_block_hash



class BlockWeb:
    def __init__(self):
        pass 


class BlockChain:
    def __init__(self, ):
        pass

    """ 
    
    """

    def add_block(self):
        """ 
            This is the main function that happen during mining
        """
    

class Block:
    def __init__(self, index, wallet_id, block_chian_id, previous_hash="000"):
        self.index = index
        self.timestamp = create_timestamp()
        self.block_id = generate_random_id()
        self.hash = self.cal_block_hash()
        self.previous_hash = previous_hash
        self.wallet_id = wallet_id
        self.block_chain_id = block_chian_id


        
    def cal_block_hash(self):
        coin_data = [
            str(self.index),
            str(self.timestamp),
            str(self.block_id),
            str(self.previous_hash),
            str(self.wallet_id),
            str(self.block_chain_id),
        ]


        data_to_be_hashed = coin_data_formatter(coin_data)
        
        return generate_block_hash(data_to_be_hashed)

    def create_block(self):
        """ 
            Block would be created and saved here
        """

    def change_wallet_id(self):
        """ 
            The would be useful for by the blockchain class to change the owner of the coin
        """




class Wallet:
    def __init__(self):
        self.wallet_id = generate_random_id()
        self.transaction_chain = []
        self.wallet_balance = self.calculate_balance()

    def calculate_balance(self):



class CoinUser:
    def __init__(self, first_name, last_name, email, phone_no, banker_name, account_no):
        self.first_name = first_name
        self.last_name = last_name
        self.user_email = email
        self.phone_no = banker_name 
        self.account_no = account_no


dc = CoinData(123, 12233, 122, 1122)
print(dc.hash)