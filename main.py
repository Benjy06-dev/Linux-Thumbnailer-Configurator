import os

def main():
    print("Linux Thumbnailer Configurator")
    print("by benjy")
    print("\n[ACTIVITY MONITOR]")
    print("PLEASE RUN AS SUDO!")
    
    # define thumbnailer path
    thumbnailers_path = r"/usr/share/thumbnailers"
    
    # check if dir exists
    print("Checking Thumbnailers directory")
    if not os.path.isdir(thumbnailers_path):
        raise Exception(f"Thumbnailers path not found! {thumbnailers_path}")
    
    print("Directory initialized!")
    
    # for loop
    def _fetch_files(print_files:bool = True) -> list:
        dir_files = sorted(os.listdir(thumbnailers_path))
        print("Files were refreshed")
        if print_files:
            print("\n")	
            for idx, file in enumerate(dir_files):
                print(f"{idx}. {file}")
            print("\n")
        return dir_files
          
    # user loop
    while True:
        files = _fetch_files()
        usr = input("[R]efresh files | [C]hange state | [E]nable All | [D]isable all >")
        
        match usr.lower():
            case "r":
                continue
            
            case "c":
                while True:
                    file_amount = len(files)
                    selection = input(f"Choose file 0-{file_amount-1} >")
                    
                    if selection.lower() in ["exit", "quit", "q"]:
                        print("Action aborted!")
                        break
                    
                    # convert to int
                    try:
                        selection = int(selection)
                    except ValueError:
                        print("False Input!")
                        continue
                    
                    if not 0 <= selection <= file_amount - 1:
                        print("False Input!")
                        continue
                    break
                
                # determine state
                file_state = True
                if files[selection].endswith(".disabled"):
                    file_state = False
                
                # confirmation
                x = input(f"Are you sure you want to {'disable' if file_state else 'enable'} [Y/N] >")
                if x.lower() == "y":
                    file_path = os.path.join(thumbnailers_path, files[selection])
                    
                    # determine ne file path
                    if file_state:
                        renamed_path = file_path + ".disabled"
                    else:
                        renamed_path = file_path.rstrip(".disabled")
                        
                    # rename
                    os.rename(file_path, renamed_path)
                    print("complete.")
                else:
                    print("Action aborted!")
            
            case "e":
                # confirmation
                x = input(f"Are you sure you want to enable all thumbnailers? [Y/N] >")
                if x.lower() == "y":
                    for file in files:
                        file_path = os.path.join(thumbnailers_path, file)
                        # determine state
                        file_state = True
                        if file.endswith(".disabled"):
                            file_state = False
                        
                        if not file_state:
                            renamed_path = file_path.rstrip(".disabled")
                            # rename
                            os.rename(file_path, renamed_path)
                    print("complete.")
                          
            case "d":
                # confirmation
                x = input(f"Are you sure you want to disable all thumbnailers? [Y/N] >")
                if x.lower() == "y":
                    for file in files:
                        file_path = os.path.join(thumbnailers_path, file)
                        # determine state
                        file_state = True
                        if file.endswith(".disabled"):
                            file_state = False
                        
                        if file_state:
                            renamed_path = file_path + ".disabled"
                            # rename
                            os.rename(file_path, renamed_path)
                    print("complete.")
                        
                else:
                    print("Action aborted!")
            
            case _:
                print("False Input!")
    

if __name__ == "__main__":
    main()