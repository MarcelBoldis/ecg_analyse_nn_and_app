path_to_database = '../mit-bih-arrhythmia-database-1.0.0'
path_to_images = '../image_data'
path_to_dataset_from_images = '../dataset_from_images'


# Normal beat - NOR - N
# Atrial premature contraction beat - APC - A
# Premature ventricular contraction - PVC - V
# Paced beat - PAB - /
# Right bundle branch block beat - RBB - R
# Left bundle branch block beat - LBB - L
# Ventricular escape beat - VEB - E
all_beats = ['N', 'A', 'V', '/', 'R', 'L', 'E']
abnormal_beats = ['A', 'V', '/', 'R', 'L', 'E']
all_abnormal_beats = ['L', 'R', 'V', '/', 'A', 'f', 'F', 'j', 'a', 'E', 'e', 'J', 'S']

arrhythmia_signals = ['NOR', 'APC', 'PVC', 'PAB', 'RBB', 'LBB', 'VEB']

dataset = ['100', '101', '102', '103', '104', '105', '106', '107',
       '108', '109', '111', '112', '113', '114', '115', '116',
       '117', '118', '119', '121', '122', '123', '124', '200',
       '201', '202', '203', '205', '207', '208', '209', '210',
       '212', '213', '214', '215', '217', '219', '220', '221',
       '222', '223', '228', '230', '231', '232', '233', '234']

image_size = (128, 128)
