import tqdm,os,subprocess

def main() -> None:
    #os.chdir("AHC/ahc033")
    f = open("./AHC/ahc033/res.csv","w")
    f.write("num,score\n")
    for num in tqdm.tqdm(range(100)):
        run_file_name = "./a/a.py"
        env_file = "./tools/"
        input_file_name = "./tools/in/{:0=4}.txt".format(num)
        output_file_name = "./output.txt"
        subprocess.run(f"pypy {run_file_name} < {input_file_name} > {output_file_name}",shell=True,text=True,cwd="./AHC/ahc033/")
        input_file_name = "./in/{:0=4}.txt".format(num)
        output_file_name = "../output.txt"
        #os.chdir(env_file)
        score_str = subprocess.run(f"cargo run -r --bin vis {input_file_name} {output_file_name}",shell=True,text=True,capture_output=True,cwd="./AHC/ahc033/tools/").stdout
        score = score_str.split("\n")[-2]
        score = int(score.split("=")[-1])
        f.write(f"{num},{score}\n")
        #os.chdir("../")
    #os.chdir("../../")
if __name__=="__main__":
    main()