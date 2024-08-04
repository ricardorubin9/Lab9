""" 
Description: 
  Graphical user interface that displays select information about a 
  user-specified Pokemon fetched from the PokeAPI 

Usage:
  python poke_info_viewer.py
"""
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from poke_api import get_pokemon_info


# Create the main window
root = Tk()
root.title("Pokemon Information")
root.resizable(False, False)

# TODO: Create the frames
frm_input = ttk.Frame(root)
frm_input.grid(row=0, column =0, columnspan=2, pady=(20,10))

## frame for Info
frm_info = ttk.LabelFrame(root, text="Info")
frm_info.grid(row=1, column = 0, padx=(20,10), pady=(10,20), sticky=N)

## Frame for stats
frm_stats = ttk.LabelFrame(root, text="Stats")
frm_stats.grid(row=1, column = 1, padx=(10,20), pady=(10,20), sticky=N)

# TODO: Populate the user input frame with widgets
lbl_name = ttk.Label (frm_input, text="Pokemon Name:")
lbl_name.grid(row=0, column=0, padx=(10,5), pady=10)

enter_name =  ttk.Entry(frm_input)
enter_name.insert(0, "Diglett")
enter_name.grid(row=0, column=1)

def handle_btn_get_info():
    poke_name = enter_name.get().strip()
    if poke_name == '': return 
    poke_info = get_pokemon_info(poke_name)
    if poke_info:
        lbl_height_val['text'] = str(poke_info['height']) + ' dm'
        #DO FOR Weight
        lbl_weight_val['text'] = str(poke_info['weight']) + ' hg'

        types_list = [t['type']['name'].capitalize() for t in poke_info['types']]
       
        #-----stats
        lbl_type_val['text'] = ', '.join(types_list)
        bar_hp['value'] = poke_info['stats'][0]['base_stat']
        bar_attack['value'] = poke_info['stats'][1]['base_stat']
        ##Finish the rest!!
        bar_defense['value'] = poke_info['stats'][2]['base_stat']
        #bar_defense
        bar_sa['value'] = poke_info['stats'][3]['base_stat']
        #bar_special_attack
        bar_sd['value'] = poke_info['stats'][4]['base_stat']
        #bar_special_defense
        bar_speed['value'] = poke_info['stats'][5]['base_stat']
        #bar_speed
    else:
        error_message = f"Unable to fetch information for {poke_name} from the PokeAPI."
        messagebox.showinfo(title ='Error', message =  error_message, icon='error')

btn_get_info =ttk.Button(root, text="Get info", command=handle_btn_get_info)
btn_get_info.grid(row=0, column=2, padx=10, pady=10)


#populate the info frame with widgets
lbl_height= ttk.Label(frm_info, text="Height: ")
lbl_height.grid(row=2, column = 1, padx=(20,10), pady=(10,20), sticky=N)
lbl_height_val = ttk.Label(frm_info, width =20)
lbl_height_val.grid(row=2, column = 2, padx=(20,10), pady=(10,20), sticky=N)

## Do the same for Weight
lbl_weight = ttk.Label(frm_info, text="Weight: ")
lbl_weight.grid(row=3, column = 1, padx=(20,10), pady=(10,20), sticky=N)
lbl_weight_val = ttk.Label(frm_info, width =20)
lbl_weight_val.grid(row=3, column = 1, padx=(20,10), pady=(10,20), sticky=N)

lbl_type = ttk.Label(frm_info, text="Type: ")
lbl_type.grid(row=4, column = 1, padx=(20,10), pady=(10,20), sticky=N)
lbl_type_val = ttk.Label(frm_info, width =20)
lbl_type_val.grid(row=4, column = 1, padx=(20,10), pady=(10,20), sticky=N)

##Stats frame
STATE_MAX_VALUE = 255.0
PRG_BAR_LENGHT = 200

label_hp = ttk.Label(frm_stats, text = "HP:")
label_hp.grid(row=0, column=0, padx=(10,5), pady=(10,5), sticky=E)
bar_hp = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_hp.grid(row=0, column=1, padx=(0,10), pady=(10,5))

lbl_attack = ttk.Label(frm_stats, text="Attack:")
lbl_attack.grid(row=1, column=0, padx=(10,5), pady=5, sticky=E)
bar_attack = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_attack.grid(row=1, column=1, padx=(0,10), pady=5)

lbl_defense = ttk.Label(frm_stats, text="Defense:")
lbl_defense.grid(row=2, column=0, padx=(10,5), pady=5, sticky=E)
bar_defense = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_defense.grid(row=2, column=1, padx=(0,10), pady=5)
## Do the same for Defense, Special attack, Special Defense

lbl_sa = ttk.Label(frm_stats, text="Special Attack:")
lbl_sa.grid(row=3, column=0, padx=(10,5), pady=5, sticky=E)
bar_sa = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_sa.grid(row=3, column=1, padx=(0,10), pady=5)

lbl_sd = ttk.Label(frm_stats, text="Special Defense:")
lbl_sd.grid(row=4, column=0, padx=(10,5), pady=5, sticky=E)
bar_sd = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_sd.grid(row=4, column=1, padx=(0,10), pady=5)

lbl_speed = ttk.Label(frm_stats, text="Speed:")
lbl_speed.grid(row=5, column=0, padx=(10,5), pady=5, sticky=E)
bar_speed = ttk.Progressbar(frm_stats, length=PRG_BAR_LENGHT, maximum=STATE_MAX_VALUE)
bar_speed.grid(row=5, column=1, padx=(0,10), pady=5)

root.mainloop()