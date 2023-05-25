from scrapy import cmdline
from multiprocessing import Process

def run_cmds(cmd="scrapy crawl GpusVideoGraphicsCards -a pages=1,100"):     
    print(cmd + "\n")                                                        
    cmdline.execute(cmd.split())

if __name__ == "__main__":  # confirms that the code is under main function
    cmds = []
    step = 5
    minVal = 1
    for maxVal in range(1 + step, 100 + 1 + step, step):
        cmd = "scrapy crawl GpusVideoGraphicsCards -a pages="+ str(minVal) + "," + str(maxVal - 1) + " --nolog"
        cmds.append(cmd)
        minVal = maxVal

    procs = []
    # instantiating process with arguments
    for cmd in cmds:
        proc = Process(target=run_cmds, args=(cmd,))
        procs.append(proc)
        proc.start()

    # complete the processes
    for proc in procs:
        proc.join()