def count_smileys(arr):
    smiles = []
    count = 0
    for eyes in [';', ':']:
        for nose in ['-', '~', '']:
            for mouth in [')', 'D']:
                smiles.append(eyes + nose + mouth)
    for example in arr:
        for smile in smiles:
            count += example.count(smile)
    return count