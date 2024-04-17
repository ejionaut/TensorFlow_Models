# -*- coding: utf-8 -*-
# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: faster_rcnn.proto
# Protobuf Python Version: 5.26.1
"""Generated protocol buffer code."""
from google.protobuf import descriptor as _descriptor
from google.protobuf import descriptor_pool as _descriptor_pool
from google.protobuf import symbol_database as _symbol_database
from google.protobuf.internal import builder as _builder
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()


from object_detection.protos import anchor_generator_pb2 as anchor__generator__pb2
from object_detection.protos import box_predictor_pb2 as box__predictor__pb2
from object_detection.protos import hyperparams_pb2 as hyperparams__pb2
from object_detection.protos import image_resizer_pb2 as image__resizer__pb2
from object_detection.protos import losses_pb2 as losses__pb2
from object_detection.protos import post_processing_pb2 as post__processing__pb2
from object_detection.protos import fpn_pb2 as fpn__pb2


DESCRIPTOR = _descriptor_pool.Default().AddSerializedFile(b'\n\x11\x66\x61ster_rcnn.proto\x12\x17object_detection.protos\x1a\x16\x61nchor_generator.proto\x1a\x13\x62ox_predictor.proto\x1a\x11hyperparams.proto\x1a\x13image_resizer.proto\x1a\x0closses.proto\x1a\x15post_processing.proto\x1a\tfpn.proto\"\x97\x10\n\nFasterRcnn\x12\x1b\n\x10number_of_stages\x18\x01 \x01(\x05:\x01\x32\x12\x13\n\x0bnum_classes\x18\x03 \x01(\x05\x12<\n\rimage_resizer\x18\x04 \x01(\x0b\x32%.object_detection.protos.ImageResizer\x12N\n\x11\x66\x65\x61ture_extractor\x18\x05 \x01(\x0b\x32\x33.object_detection.protos.FasterRcnnFeatureExtractor\x12N\n\x1c\x66irst_stage_anchor_generator\x18\x06 \x01(\x0b\x32(.object_detection.protos.AnchorGenerator\x12\"\n\x17\x66irst_stage_atrous_rate\x18\x07 \x01(\x05:\x01\x31\x12X\n*first_stage_box_predictor_conv_hyperparams\x18\x08 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12\x30\n%first_stage_box_predictor_kernel_size\x18\t \x01(\x05:\x01\x33\x12,\n\x1f\x66irst_stage_box_predictor_depth\x18\n \x01(\x05:\x03\x35\x31\x32\x12\'\n\x1a\x66irst_stage_minibatch_size\x18\x0b \x01(\x05:\x03\x32\x35\x36\x12\x32\n%first_stage_positive_balance_fraction\x18\x0c \x01(\x02:\x03\x30.5\x12*\n\x1f\x66irst_stage_nms_score_threshold\x18\r \x01(\x02:\x01\x30\x12*\n\x1d\x66irst_stage_nms_iou_threshold\x18\x0e \x01(\x02:\x03\x30.7\x12&\n\x19\x66irst_stage_max_proposals\x18\x0f \x01(\x05:\x03\x33\x30\x30\x12/\n$first_stage_localization_loss_weight\x18\x10 \x01(\x02:\x01\x31\x12-\n\"first_stage_objectness_loss_weight\x18\x11 \x01(\x02:\x01\x31\x12\x19\n\x11initial_crop_size\x18\x12 \x01(\x05\x12\x1b\n\x13maxpool_kernel_size\x18\x13 \x01(\x05\x12\x16\n\x0emaxpool_stride\x18\x14 \x01(\x05\x12I\n\x1asecond_stage_box_predictor\x18\x15 \x01(\x0b\x32%.object_detection.protos.BoxPredictor\x12#\n\x17second_stage_batch_size\x18\x16 \x01(\x05:\x02\x36\x34\x12+\n\x1dsecond_stage_balance_fraction\x18\x17 \x01(\x02:\x04\x30.25\x12M\n\x1csecond_stage_post_processing\x18\x18 \x01(\x0b\x32\'.object_detection.protos.PostProcessing\x12\x30\n%second_stage_localization_loss_weight\x18\x19 \x01(\x02:\x01\x31\x12\x32\n\'second_stage_classification_loss_weight\x18\x1a \x01(\x02:\x01\x31\x12\x33\n(second_stage_mask_prediction_loss_weight\x18\x1b \x01(\x02:\x01\x31\x12\x45\n\x12hard_example_miner\x18\x1c \x01(\x0b\x32).object_detection.protos.HardExampleMiner\x12U\n second_stage_classification_loss\x18\x1d \x01(\x0b\x32+.object_detection.protos.ClassificationLoss\x12\'\n\x18inplace_batchnorm_update\x18\x1e \x01(\x08:\x05\x66\x61lse\x12)\n\x1ause_matmul_crop_and_resize\x18\x1f \x01(\x08:\x05\x66\x61lse\x12$\n\x15\x63lip_anchors_to_image\x18  \x01(\x08:\x05\x66\x61lse\x12+\n\x1cuse_matmul_gather_in_matcher\x18! \x01(\x08:\x05\x66\x61lse\x12\x30\n!use_static_balanced_label_sampler\x18\" \x01(\x08:\x05\x66\x61lse\x12 \n\x11use_static_shapes\x18# \x01(\x08:\x05\x66\x61lse\x12\x1a\n\x0cresize_masks\x18$ \x01(\x08:\x04true\x12)\n\x1ause_static_shapes_for_eval\x18% \x01(\x08:\x05\x66\x61lse\x12\x30\n\"use_partitioned_nms_in_first_stage\x18& \x01(\x08:\x04true\x12\x33\n$return_raw_detections_during_predict\x18\' \x01(\x08:\x05\x66\x61lse\x12.\n\x1fuse_combined_nms_in_first_stage\x18( \x01(\x08:\x05\x66\x61lse\x12(\n\x19output_final_box_features\x18* \x01(\x08:\x05\x66\x61lse\x12,\n\x1doutput_final_box_rpn_features\x18+ \x01(\x08:\x05\x66\x61lse\x12\x38\n\x0e\x63ontext_config\x18) \x01(\x0b\x32 .object_detection.protos.Context\"\xbd\x03\n\x07\x43ontext\x12&\n\x18max_num_context_features\x18\x01 \x01(\x05:\x04\x32\x30\x30\x30\x12,\n\x1e\x61ttention_bottleneck_dimension\x18\x02 \x01(\x05:\x04\x32\x30\x34\x38\x12#\n\x15\x61ttention_temperature\x18\x03 \x01(\x02:\x04\x30.01\x12$\n\x16\x63ontext_feature_length\x18\x04 \x01(\x05:\x04\x32\x30\x35\x37\x12!\n\x12use_self_attention\x18\x06 \x01(\x08:\x05\x66\x61lse\x12%\n\x17use_long_term_attention\x18\x07 \x01(\x08:\x04true\x12)\n\x1aself_attention_in_sequence\x18\x08 \x01(\x08:\x05\x66\x61lse\x12\x1e\n\x13num_attention_heads\x18\t \x01(\x05:\x01\x31\x12\x1f\n\x14num_attention_layers\x18\x0b \x01(\x05:\x01\x31\x12[\n\x12\x61ttention_position\x18\n \x01(\x0e\x32*.object_detection.protos.AttentionPosition:\x13POST_BOX_CLASSIFIER\"\xcf\x02\n\x1a\x46\x61sterRcnnFeatureExtractor\x12\x0c\n\x04type\x18\x01 \x01(\t\x12\'\n\x1b\x66irst_stage_features_stride\x18\x02 \x01(\x05:\x02\x31\x36\x12#\n\x14\x62\x61tch_norm_trainable\x18\x03 \x01(\x08:\x05\x66\x61lse\x12>\n\x10\x63onv_hyperparams\x18\x04 \x01(\x0b\x32$.object_detection.protos.Hyperparams\x12:\n+override_base_feature_extractor_hyperparams\x18\x05 \x01(\x08:\x05\x66\x61lse\x12\x1b\n\x0fpad_to_multiple\x18\x06 \x01(\x05:\x02\x33\x32\x12<\n\x03\x66pn\x18\x07 \x01(\x0b\x32/.object_detection.protos.FeaturePyramidNetworks*Q\n\x11\x41ttentionPosition\x12\x15\n\x11\x41TTENTION_DEFAULT\x10\x00\x12\x17\n\x13POST_BOX_CLASSIFIER\x10\x01\x12\x0c\n\x08POST_RPN\x10\x02')

_globals = globals()
_builder.BuildMessageAndEnumDescriptors(DESCRIPTOR, _globals)
_builder.BuildTopDescriptorsAndMessages(DESCRIPTOR, 'faster_rcnn_pb2', _globals)
if not _descriptor._USE_C_DESCRIPTORS:
  DESCRIPTOR._loaded_options = None
  _globals['_ATTENTIONPOSITION']._serialized_start=3039
  _globals['_ATTENTIONPOSITION']._serialized_end=3120
  _globals['_FASTERRCNN']._serialized_start=180
  _globals['_FASTERRCNN']._serialized_end=2251
  _globals['_CONTEXT']._serialized_start=2254
  _globals['_CONTEXT']._serialized_end=2699
  _globals['_FASTERRCNNFEATUREEXTRACTOR']._serialized_start=2702
  _globals['_FASTERRCNNFEATUREEXTRACTOR']._serialized_end=3037
# @@protoc_insertion_point(module_scope)
