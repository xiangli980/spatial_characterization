python run_infer.py \
--gpu='1' \
--nr_types=3 \
--type_info_path=./type_info.json \
--model_mode=original \
--model_path=./logs/net_epoch=50.tar \
tile \
--input_dir=./dataset/ \
--output_dir=./exp_output/ \
--mem_usage=0.2 \

