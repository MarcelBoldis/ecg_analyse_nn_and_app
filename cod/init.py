try:
    import sys
    import pandas as pd
    from cod.plot_data import plot_graph
    from cod.extension import dataset, arrhythmia_signals
    from cod.create_images import create_images
    from cod.data_augmentation import data_augmentation
    from cod.additional_functions_for_cnn import load_data
    from cod.save_data_to_file import save_data_to_file
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


if __name__ == "__main__":
    df = pd.DataFrame()
    for count, dis in enumerate(arrhythmia_signals):
        pict_order = 0
        for person in dataset:
            rec_signal, ant_symbol, ant_sample, bad_signal = load_data(person)
            pict_order = create_images(ant_symbol, ant_sample, rec_signal, person, arrhythmia_signals[count], count, pict_order)
            plot_graph(rec_signal, ant_sample, bad_signal)

    # data_augmentation()
    save_data_to_file()
