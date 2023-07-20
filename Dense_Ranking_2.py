def dense_ranking(scores, gits_scores):
    scores = sorted(set(scores), reverse=True)
    ranks = []
    
    for score in gits_scores:
        rank = 1
        for s in scores:
            if score < s:
                rank += 1
            else:
                break
        ranks.append(rank)
    
    return ranks

if __name__ == "__main__":
    try:
        total_players = int(input("Masukkan jumlah pemain: "))
        scores = list(map(int, input("Masukkan daftar skor pemain (dipisahkan dengan spasi): ").split()))
        num_games = int(input("Masukkan jumlah permainan yang diikuti oleh GITS: "))
        gits_scores = list(map(int, input("Masukkan skor permainan GITS (dipisahkan dengan spasi): ").split()))

        if len(scores) != total_players:
            print("Jumlah pemain tidak sesuai dengan jumlah skor yang dimasukkan!")
        else:
            ranks = dense_ranking(scores, gits_scores)
            print("Sampel Output:")
            print(*ranks)
    except ValueError:
        print("Input yang salah! Pastikan Anda memasukkan angka dengan benar.")