import csv

# Example list of files/offsets (fill in as needed):
file_info = [
    # {
    #     "csv_path": "audio/cc_19_rosa.csv",
    #     "offset_ms": 1000 * 1000,  # 1000 seconds
    #     "output_path": "audio/cc_19_rosa_parsed.txt"
    # },
    # {
    #     "csv_path": "audio/carrion_crow_19_AL_Azul_1015truncated.csv",
    #     "offset_ms": 139 * 1000,   # 139 seconds
    #     "output_path": "audio/cc_19_azul_parsed.txt"
    # },
    # {
    #     "csv_path": "audio/carrion_crow_19_AL_Naranja_1006truncated.csv",
    #     "offset_ms": 1273 * 1000,  # 1273 seconds
    #     "output_path": "audio/cc_19_naranja_parsed.txt"
    # },

    {
        "csv_path": "audio/Spiders_007.csv",
        "offset_ms": 12 * 1000,  # 1273 seconds
        "output_path": "audio/Spiders_007_parsed.txt"
    },
    {
        "csv_path": "audio/Spiders_011.csv",
        "offset_ms": 101 * 1000,  # 1273 seconds
        "output_path": "audio/Spiders_011_parsed.txt"
    },

]

for fobj in file_info:
    offset_s = fobj["offset_ms"] / 1000.0  # convert ms to seconds
    start_cut = offset_s
    end_cut = offset_s + 30.0
    
    # Read the CSV
    rows = []
    with open(fobj["csv_path"], "r") as fin:
        reader = csv.DictReader(fin)
        for line in reader:
            st = float(line["Starttime"])
            et = float(line["Endtime"])
            # Filter based on offset
            if st >= start_cut and st < end_cut:
                # Adjust times
                new_st = st - offset_s
                new_et = et - offset_s
                rows.append((new_st, new_et))
    
    # Write out in desired format
    with open(fobj["output_path"], "w") as fout:
        fout.write("Begin Time (s)\tEnd Time (s)\tAnnotation\n")
        for (new_st, new_et) in rows:
            fout.write(f"{new_st}\t{new_et}\tPOS\n")
