import os

def export_vcard(vc_final, single_file):
    """
    Exporting a vCard to /export/
    """
    try:
        file_name = f"export/{vc_final['filename']}" if not single_file else f"export/final_export.vcf"
        with open(file_name, "a") as f:
            f.write(vc_final['output'])
            f.close()
            print(f"Created vCard 3.0 for {vc_final['name']}.")
    except IOError:
        print(f"I/O error for {vc_final['filename']}")


def check_export():
    """
    Checks if export folder exists in directory
    """
    if not os.path.exists("export"):
        print("Creating /export folder...")
        os.makedirs("export")
