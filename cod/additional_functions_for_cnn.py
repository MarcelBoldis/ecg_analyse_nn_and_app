try:
    import sys
    import wfdb
    from cod.extension import abnormal_beats, path_to_database
except ValueError:
    print("Modules loading failed in " + sys.argv[0])


def load_data(pr):
    try:
        file_name = path_to_database + '/' + pr
        record = wfdb.rdrecord(record_name=file_name)
        annotations = wfdb.rdann(file_name, 'atr')
        rec_signal = record.p_signal[:, 0]
        ant_symbol = annotations.symbol
        ant_sample = annotations.sample

        bad_signal = []
        for item, position in zip(ant_symbol, ant_sample):
            if item in abnormal_beats:
                bad_signal.append(position)

        return rec_signal, ant_symbol, ant_sample, bad_signal

    except ValueError:
        print('Error while loading data!')