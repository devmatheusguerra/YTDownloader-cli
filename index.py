from pytube import YouTube
import sys
import os

def Download(link, output):
    youtubeObject = YouTube(link)
    youtubeObject = youtubeObject.streams.get_highest_resolution()
    try:
        current_directory = os.getcwd()
        print("Saving to: " + current_directory + "/" + output)
        youtubeObject.download(str(output))
        print("Download is completed successfully")
    except:
        print("An error has occurred")

def main():
    # Get the URL from the command line
    output = "./"
    url = ""
    args = sys.argv
    for param in args:
        if param == "--url" or param == "-u":
            url = args[args.index(param) + 1]
        
        if param == "--output" or param == "-o":
            print("Output directory: " + args[args.index(param) + 1])
            output = args[args.index(param) + 1]

        if param == "--version" or param == "-v":
            sys.stdout.write("\x1b[2J\x1b[H")
            print("YtDownloader-cli v1.0.0")
            return
        
        if param == "--help" or param == "-h":
            # Clear the console
            sys.stdout.write("\x1b[2J\x1b[H")
            print("Usage: python index.py [options]")
            print("Options:")
            print("--url, -u: The url of the video to download")
            print("--output, -o: The output directory")
            print("--version, -v: The version of the program")
            print("--help, -h: The help menu")
            return

    try:
        Download(url, output)
    except:
        sys.stdout.write("\x1b[2J\x1b[H")
        print("Usage: python index.py [options]")
        print("Options:")
        print("--url, -u: The url of the video to download")
        print("--output, -o: The output directory")
        return
    

if __name__ == "__main__":
    main()