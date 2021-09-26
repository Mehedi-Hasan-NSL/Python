from dataclasses import dataclass

@dataclass
class Config:
	BATCH_SIZE = 128
	LR = 0.001
	NUM_LAYERS = 1
	FILTER_SIZE = 32
	KERNEL_SIZE = (3, 3)
config = Config()