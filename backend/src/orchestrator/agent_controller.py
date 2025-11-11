from src.agents.writer_agent import run_writer
from src.agents.designer_agent import run_designer
from src.agents.reviewer_agent import run_reviewer
from src.agents.compliance_agent import run_compliance
from src.agents.publisher_agent import run_publisher
from src.utils.memory_store import save_memory
from src.utils.logger import log_event

def run_pipeline(prompt: str):
    log_event("Controller", f"Starting content generation pipeline for: '{prompt}'")

    # 1️⃣ Writer
    draft = run_writer(prompt)
    save_memory("writer", draft)
    log_event("Writer", "Generated initial draft.")

    # 2️⃣ Designer
    image_path = run_designer(draft)
    save_memory("designer", image_path)
    log_event("Designer", "Generated visual.")

    # 3️⃣ Reviewer
    review = run_reviewer(draft)
    save_memory("reviewer", review)
    log_event("Reviewer", str(review["feedback"]))

    if not review["approved"]:
        log_event("Controller", "Review not approved. Exiting early.")
        return

    # 4️⃣ Compliance
    compliance = run_compliance(draft)
    save_memory("compliance", compliance)
    log_event("Compliance", str(compliance))

    if not compliance["approved"]:
        log_event("Controller", "Compliance failed. Stopping pipeline.")
        return

    # 5️⃣ Publisher
    result = run_publisher(draft, image_path)
    save_memory("publisher", result)
    log_event("Publisher", "Final post saved successfully.")
