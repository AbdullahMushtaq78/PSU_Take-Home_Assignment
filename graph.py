import matplotlib.pyplot as plt
import numpy as np
import matplotlib.patheffects as PathEffects

episodes = np.array([1, 2, 3, 4, 5])
success = np.array([1, 1, 1, 1, 0])  # 1: True, 0: False
accuracy = np.array([100, 100, 100, 100, 80])
task_id = 1
task_prompt = "pick up the alphabet soup and place it in the basket"

success_colors = np.array(["#189638" if s else "#D93636" for s in success])  
bg_color = "#F7F7FA"
fg_color = "#202124"
accent = "#1877E8"
font_family = "DejaVu Sans"
grid_color = "#b1b1b1"
subtitle_color = "#1877E8"

plt.style.use('default')
plt.rcParams['axes.facecolor'] = bg_color
plt.rcParams['figure.facecolor'] = bg_color
plt.rcParams['xtick.color'] = fg_color
plt.rcParams['ytick.color'] = fg_color
plt.rcParams['axes.labelcolor'] = fg_color
plt.rcParams['axes.titleweight'] = 'bold'
plt.rcParams['axes.edgecolor'] = "#d4d4d4"
plt.rcParams['font.family'] = font_family

fig, ax = plt.subplots(figsize=(9, 5.8), dpi=110)
line, = ax.plot(episodes, accuracy, color=accent, linewidth=3.2, zorder=1, alpha=0.88)
sc = ax.scatter(episodes, accuracy, s=240, c=success_colors, edgecolor=fg_color, linewidth=2, zorder=2)

for i, (ep, acc, succ) in enumerate(zip(episodes, accuracy, success)):
    label = f"Ep {ep}\n{acc}%\n{'✓' if succ else '✗'}"
    color = '#25a767' if succ else '#e06161'
    txt = ax.text(ep, acc+5, label, ha='center', va='bottom', fontsize=13, fontweight='bold', color=color, alpha=0.92)
    txt.set_path_effects([PathEffects.withStroke(linewidth=2.2, foreground=bg_color)])

ax.grid(axis='y', color=grid_color, linestyle='--', alpha=0.41)
ax.set_axisbelow(True)
ax.set_xlim(0.6, 5.4)
ax.set_ylim(0, 110)
ax.set_xticks(episodes)
ax.set_xlabel("Episode", fontsize=14, fontweight='medium', color=accent, labelpad=10)
ax.set_ylabel("Accuracy (%)", fontsize=14, fontweight='medium', color=accent, labelpad=10)

title = "OpenVLA Replication – Per-Episode Accuracy with Success/Failure"
ax.set_title(title, fontsize=18, fontweight='bold', color=fg_color, pad=38)

subtitle = (
    f"Task ID: {task_id}   |   "
    f"Prompt: '{task_prompt}'"
)
plt.suptitle(subtitle, y=0.9, fontsize=13.8, color=subtitle_color, alpha=0.94, fontweight='medium')

import matplotlib.lines as mlines
leg1 = mlines.Line2D([], [], color='#189638', marker='o', linestyle='None',
                     markersize=13, label='Success', markeredgecolor=fg_color, markeredgewidth=2)
leg2 = mlines.Line2D([], [], color='#D93636', marker='o', linestyle='None',
                     markersize=13, label='Failure', markeredgecolor=fg_color, markeredgewidth=2)

leg = plt.legend(handles=[leg1, leg2], loc='lower right', fontsize=13.2, frameon=True, borderpad=0.7)
leg.get_frame().set_facecolor('#FFF5DD')
leg.get_frame().set_edgecolor(fg_color)
plt.setp(leg.get_texts(), color=fg_color)

plt.tight_layout(rect=[0, 0, 1, 0.93])
plt.savefig("openvla_replication_accuracy_per_episode.png", dpi=300, bbox_inches='tight')
plt.show()