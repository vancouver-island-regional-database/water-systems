import fitz  # PyMuPDF
import os

# --- CONFIGURATION PATHS ---
RAW_FOLDER = "/Users/betheapenny/Documents/Github/VIRD/raw_documents"
GITHUB_FOLDER = "/Users/betheapenny/Documents/Github/VIRD/vird-water-systems/files"

# List any personal words you want destroyed from the visible text layer
TERMS_TO_REDACT = ["betheapenny", "bethearielle@gmail.com", "Bethea Penny", "BPenny", "bpenny"]

# Ensure destination folder exists
if not os.path.exists(GITHUB_FOLDER):
    os.makedirs(GITHUB_FOLDER)

def scrub_pdf(file_path, output_path):
    doc = fitz.open(file_path)
    
    # 1. Clear visible text content matches
    for page in doc:
        for term in TERMS_TO_REDACT:
            text_instances = page.search_for(term)
            for inst in text_instances:
                # Place a black redaction bar over the text
                page.add_redact_annot(inst, fill=(0, 0, 0))
        # Destroy the text layer completely underneath the bars
        page.apply_redactions()

    # 2. Complete wipe of the hidden metadata dictionary
    empty_metadata = {key: "" for key in doc.metadata.keys()}
    doc.set_metadata(empty_metadata)
    
    # 3. Save optimized, fully sanitized file
    doc.save(output_path, garbage=4, deflate=True)
    doc.close()

# Process every PDF in your input folder
if __name__ == "__main__":
    print("Starting document scrubbing...")
    for filename in os.listdir(RAW_FOLDER):
        if filename.lower().endswith(".pdf"):
            raw_path = os.path.join(RAW_FOLDER, filename)
            clean_path = os.path.join(GITHUB_FOLDER, filename)
            
            try:
                scrub_pdf(raw_path, clean_path)
                print(f"[SUCCESS] Cleaned and moved: {filename}")
            except Exception as e:
                print(f"[ERROR] Failed to process {filename}: {str(e)}")
    print("Scrubbing process finished.")