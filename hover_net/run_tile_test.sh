python run_infer.py \
--gpu='1' \
--nr_types=3 \
--type_info_path=type_info.json \
--model_mode=original \
--model_path=./logs/net_epoch=50.tar \
--nr_inference_workers=8 \
--nr_post_proc_workers=16 \
tile \
--input_dir=./data_4mouse \
--output_dir=./output_4mouse \


