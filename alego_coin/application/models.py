from django.db import models


class BlockModel(models.Model):
    block_index = models.CharField(max_length=255, unique=True)
    block_timestamp = models.CharField(max_length=255)
    block_id = models.CharField(max_length=255)
    block_hash = models.CharField(max_length=255)
    block_previous_hash = models.CharField(max_length=255)
    block_wallet_id = models.CharField(max_length=255)
    block_chain_id = models.CharField(max_length=255)

    def __str__(self):
        return f"{str(self.block_id)} - {str(self.block_wallet_id)}"