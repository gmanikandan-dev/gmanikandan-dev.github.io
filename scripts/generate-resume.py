#!/usr/bin/env python3
"""Generate gmanikandan-dev-resume.pdf from current portfolio content."""

from datetime import date
from pathlib import Path

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT
from reportlab.lib.pagesizes import letter
from reportlab.lib.styles import ParagraphStyle, getSampleStyleSheet
from reportlab.lib.units import inch
from reportlab.platypus import (
    HRFlowable,
    ListFlowable,
    ListItem,
    Paragraph,
    SimpleDocTemplate,
    Spacer,
)

OUTPUT = Path(__file__).resolve().parent.parent / "assets" / "img" / "gmanikandan-dev-resume.pdf"

start_date = date(2021, 6, 1)
today = date.today()
total_months = (today.year - start_date.year) * 12 + (today.month - start_date.month)
years = total_months // 12
months = total_months % 12
experience_label = f"{years}+ years" if months == 0 else f"{years}.{months} years"
LINK_COLOR = "#2563eb"


def link(href, text):
    return f"<a href='{href}' color='{LINK_COLOR}'>{text}</a>"


def bullet_items(items, style):
    return ListFlowable(
        [ListItem(Paragraph(item, style), leftIndent=12) for item in items],
        bulletType="bullet",
        start="•",
        leftIndent=18,
        bulletFontName="Helvetica",
        bulletFontSize=9,
    )


def build_pdf():
    doc = SimpleDocTemplate(
        str(OUTPUT),
        pagesize=letter,
        leftMargin=0.65 * inch,
        rightMargin=0.65 * inch,
        topMargin=0.55 * inch,
        bottomMargin=0.55 * inch,
    )

    styles = getSampleStyleSheet()
    name_style = ParagraphStyle(
        "Name",
        parent=styles["Heading1"],
        fontName="Helvetica-Bold",
        fontSize=20,
        leading=24,
        spaceAfter=4,
        textColor=colors.HexColor("#1a1d27"),
    )
    contact_style = ParagraphStyle(
        "Contact",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#444444"),
        spaceAfter=10,
    )
    section_style = ParagraphStyle(
        "Section",
        parent=styles["Heading2"],
        fontName="Helvetica-Bold",
        fontSize=11,
        leading=14,
        spaceBefore=10,
        spaceAfter=4,
        textColor=colors.HexColor("#1a1d27"),
    )
    job_title_style = ParagraphStyle(
        "JobTitle",
        parent=styles["Normal"],
        fontName="Helvetica-Bold",
        fontSize=10,
        leading=13,
        spaceAfter=2,
    )
    job_meta_style = ParagraphStyle(
        "JobMeta",
        parent=styles["Normal"],
        fontName="Helvetica-Oblique",
        fontSize=9,
        leading=12,
        textColor=colors.HexColor("#555555"),
        spaceAfter=4,
    )
    body_style = ParagraphStyle(
        "Body",
        parent=styles["Normal"],
        fontName="Helvetica",
        fontSize=9,
        leading=12,
        spaceAfter=6,
    )
    bullet_style = ParagraphStyle(
        "Bullet",
        parent=body_style,
        leftIndent=0,
        spaceAfter=2,
    )
    skills_style = ParagraphStyle(
        "Skills",
        parent=body_style,
        spaceAfter=3,
    )

    story = []

    story.append(Paragraph("MANIKANDAN G", name_style))
    story.append(
        Paragraph(
            "Chennai, India 600096 &nbsp;|&nbsp; +91 9629322688 &nbsp;|&nbsp; "
            f"{link('mailto:gmanikandan845@gmail.com', 'gmanikandan845@gmail.com')} &nbsp;|&nbsp; "
            f"{link('https://www.linkedin.com/in/gmanikandan-dev/', 'LinkedIn')} &nbsp;|&nbsp; "
            f"{link('https://gmanikandan-dev.github.io', 'Portfolio')} &nbsp;|&nbsp; "
            f"{link('https://github.com/gmanikandan-dev', 'GitHub')}",
            contact_style,
        )
    )
    story.append(HRFlowable(width="100%", thickness=1, color=colors.HexColor("#3dd6c3")))

    story.append(Paragraph("SUMMARY", section_style))
    story.append(
        Paragraph(
            f"Software Programmer with {experience_label} of experience building scalable Laravel/PHP "
            "backend services, REST APIs, and platform integrations for e-commerce and email marketing. "
            "Skilled in Magento, WooCommerce, Klaviyo, and email provider APIs, with hands-on work in "
            "React, Next.js, Livewire, and FilamentPHP. Focused on performance optimization, caching, "
            "and maintainable full-stack delivery.",
            body_style,
        )
    )

    story.append(Paragraph("EXPERIENCE", section_style))
    story.append(Paragraph("Software Programmer", job_title_style))
    story.append(Paragraph("TargetBay — Chennai, India &nbsp;|&nbsp; Jul 2023 – Present", job_meta_style))
    story.append(
        bullet_items(
            [
                "Designed and maintained scalable backend services using Laravel and PHP.",
                "Developed integrations with Magento, WooCommerce, Klaviyo, Gmail, Outlook, and Google Postmaster.",
                "Improved application performance through query optimization, caching, and data-processing pipelines.",
                "Built APIs and backend workflows supporting large-scale email marketing and e-commerce operations.",
                "Developed internal tools and user-facing features using React and Next.js.",
                "Leveraged AI-assisted development tools including GitHub Copilot, Cursor, Claude, and Windsurf.",
            ],
            bullet_style,
        )
    )
    story.append(Spacer(1, 6))

    story.append(Paragraph("Web Developer", job_title_style))
    story.append(
        Paragraph(
            "Synamen Thinklabs Private Limited — Chennai, India &nbsp;|&nbsp; Jun 2021 – Jul 2023",
            job_meta_style,
        )
    )
    story.append(
        bullet_items(
            [
                "Built and maintained web applications using Laravel and Yii2.",
                "Developed REST APIs and backend services for internal and customer-facing applications.",
                "Worked with Livewire, FilamentPHP, JavaScript, jQuery, Bootstrap, HTML, and CSS.",
                "Participated in the full software development lifecycle from requirement analysis to deployment.",
                "Gained experience in database design, authentication systems, package integrations, and Razorpay payments.",
            ],
            bullet_style,
        )
    )

    story.append(Paragraph("SKILLS", section_style))
    story.append(
        Paragraph(
            "<b>Backend:</b> PHP, Laravel, Yii2, REST APIs &nbsp;|&nbsp; "
            "<b>Frontend:</b> React, Next.js, Livewire, FilamentPHP, JavaScript, HTML, CSS, Bootstrap",
            skills_style,
        )
    )
    story.append(
        Paragraph(
            "<b>Integrations:</b> Magento, WooCommerce, Klaviyo, Gmail API, Outlook API, Google Postmaster",
            skills_style,
        )
    )
    story.append(
        Paragraph(
            "<b>Data &amp; Performance:</b> MySQL, MongoDB, Redis, query optimization, caching &nbsp;|&nbsp; "
            "<b>Tools:</b> Git, Ubuntu, VS Code, Cursor, Windsurf, PHPUnit",
            skills_style,
        )
    )

    story.append(Paragraph("EDUCATION", section_style))
    story.append(Paragraph("Bachelor of Technology, Information Technology", job_title_style))
    story.append(
        Paragraph(
            "Jayaraj Annapackiam CSI College of Engineering — Nazareth, Tuticorin &nbsp;|&nbsp; Sep 2020",
            job_meta_style,
        )
    )

    story.append(Paragraph("ACCOMPLISHMENTS", section_style))
    story.append(bullet_items(["Received a Shining Star Award."], bullet_style))

    story.append(Paragraph("LANGUAGES", section_style))
    story.append(
        Paragraph("Tamil: Native &nbsp;|&nbsp; English: Intermediate (B1)", body_style)
    )

    story.append(Paragraph("ACTIVITIES", section_style))
    story.append(
        bullet_items(
            [
                "Practicing typewriting on Ratatype for two years — "
                f"{link('https://www.ratatype.com/u4717179/certificate', 'Certificate')}",
            ],
            bullet_style,
        )
    )

    doc.build(story)
    print(f"Wrote {OUTPUT} ({OUTPUT.stat().st_size // 1024} KB)")


if __name__ == "__main__":
    build_pdf()
